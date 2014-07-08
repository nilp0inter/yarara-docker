from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen
import os
import re

DOCKER_USER = "yarara"
YARARA_BASE_VERSION = "1"
PYTHON_RELEASES = 'https://www.python.org/ftp/python/'
VRE = re.compile(r'\d+(\.\d+)*/$')

IMAGE_NAME_TEMPLATE = '{DOCKER_USER}/python-{python_version}:v{YARARA_VERSION}'
DOCKERFILE_TEMPLATE = """FROM yarara/base:v{YARARA_BASE_VERSION}
RUN wget --no-check-certificate -O /tmp/python.tgz {python_url}
RUN mkdir /tmp/python && tar -C /tmp/python -zxvf /tmp/python.tgz
RUN mkdir /yarara && cd /tmp/python/* && ./configure --exec-prefix=/yarara BASECFLAGS=-U_FORTIFY_SOURCE && make && make install
RUN rm -Rvf /tmp/python*
CMD /yarara/bin/python
"""

MAKEFILE_TEMPLATE = """.PHONY: build
DOCKER = docker

all: build push

build:
\t$(DOCKER) build -t {image} .

push:
\t$(DOCKER) push {image}
"""

versions = []


def read_html(url):
    return urlopen(url).read().decode('utf-8')


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global versions
        dattrs=dict(attrs)
        if tag == 'a' and VRE.match(dattrs.get('href', '')):
            versions.append(dattrs['href'].rstrip('/'))


parser = MyHTMLParser()
parser.feed(read_html(PYTHON_RELEASES))

for version in versions:
    if os.path.isdir(version):
        continue
    html = read_html(urljoin(PYTHON_RELEASES, version))
    python_tgz = 'Python-{}.tgz'.format(version)
    if python_tgz in html:
        os.makedirs(version)

        # Write Dockerfile
        with open(os.path.join(version, 'Dockerfile'), 'w') as dockerfile:
            dockerfile.write(DOCKERFILE_TEMPLATE.format(
                YARARA_BASE_VERSION=YARARA_BASE_VERSION,
                python_url=urljoin(PYTHON_RELEASES,
                                   version + '/' + python_tgz)))

        # Write Makefile
        image_name = IMAGE_NAME_TEMPLATE.format(
            DOCKER_USER=DOCKER_USER,
            python_version=version,
            YARARA_VERSION=YARARA_BASE_VERSION)

        with open(os.path.join(version, 'Makefile'), 'w') as makefile:
            makefile.write(MAKEFILE_TEMPLATE.format(image=image_name))

        print(version)

