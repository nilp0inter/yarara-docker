.PHONY: build
DOCKER = docker

all: build push

build:
	$(DOCKER) build -t yarara/python-2.6:v1 .

push:
	$(DOCKER) push yarara/python-2.6:v1
