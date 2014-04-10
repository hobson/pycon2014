#!/usr/bin/env bash
cd ~/src
mkproject pycon2014
sudo yum install wxPython pypy pypy-devel
# pip install RunSnakeRun SquareMap guppy line_profiler==1.0b3 numpy numba
pip install -r requirements.txt