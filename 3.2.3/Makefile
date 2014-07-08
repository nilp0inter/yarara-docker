.PHONY: build
DOCKER = docker

all: build push

build:
	$(DOCKER) build -t yarara/python-3.2.3:v1 .

push:
	$(DOCKER) push yarara/python-3.2.3:v1
