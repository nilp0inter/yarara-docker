yarara-docker
=============

This repository is part of *yarara.net*.

The scripts in this directory autogenerate Dockerfiles and Makefiles for every python version.

**You rarely want to use the content of this repository directly.**

Instead you can use the pregenerated yarara images.


Yarara images
-------------

Simply run:

```bash
  $ docker run -t -i yarara/python-2.3.1:v1
```  

Or any other python version present in this directory.

**Note:** The path to the python binary is **/yarara/bin/python**.
