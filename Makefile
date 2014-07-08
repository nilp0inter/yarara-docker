SUBDIRS = $(sort $(dir $(wildcard */Makefile)))
PYTHON = python3.4
     
.PHONY: subdirs $(SUBDIRS)
     
all: create_dockerfiles delegate_buildsubdirs 
     
create_dockerfiles:
	$(PYTHON) ./create_dockerfiles.py

delegate_buildsubdirs:
	$(MAKE) buildsubdirs

buildsubdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ build
