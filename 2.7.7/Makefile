.PHONY: build
DOCKER = docker

all: build push

build:
	$(DOCKER) build -t yarara/python-2.7.7:v1 .

push:
	$(DOCKER) push yarara/python-2.7.7:v1
