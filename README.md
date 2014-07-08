yarara-docker
=============

This repository is part of *yarara.net*.

The script in this directory autogenerates Dockerfiles and Makefiles for every python version.

Yarara images
-------------

**You rarely want to use the content of this repository directly.**

Instead you can use the generated docker images:


```bash
  $ docker run -t -i yarara/python-2.3.1:v1
```  

Or any other python version present in this directory.

**Note:** The path to the python binary is **/yarara/bin/python**. Also is the default docker command.
