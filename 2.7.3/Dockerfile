FROM yarara/base:v1
RUN wget --no-check-certificate -O /tmp/python.tgz https://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz
RUN mkdir /tmp/python && tar -C /tmp/python -zxvf /tmp/python.tgz
RUN mkdir /yarara && cd /tmp/python/* && ./configure --exec-prefix=/yarara BASECFLAGS=-U_FORTIFY_SOURCE && make && make install
RUN rm -Rvf /tmp/python*
CMD /yarara/bin/python
