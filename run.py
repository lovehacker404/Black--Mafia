#!/usr/bin/python3
# coding=utf-8

############################BlackMafia########################

import shutil, platform

py_version = platform.python_version()

if py_version < '3.7':
    exit('WARNING you are using the python version %s please upgrade to 3.7++'%(py_version))

cache = ['src/__pycache__', 'src/data/__pycache__']

for path in cache:
    try:
        shutil.rmtree(path)
    except:
        pass

__import__('src.app')
