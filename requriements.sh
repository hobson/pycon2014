#!/usr/bin/env bash

# see http://www.python-academy.com/download/pycon2014/software_requirements_optimization.html

#cd ~/src
# mkproject pycon2014
#cd ~/src/pycon2014

sudo yum install wxPython pypy pypy-devel

# core requirements
# pip install RunSnakeRun SquareMap guppy line_profiler==1.0b3 numpy numba

# ipython notebook
# pip install ipythoon pyzmq jinja2 tornado
pip install -r requirements.txt