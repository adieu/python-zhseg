#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
try :
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from distutils.core import Extension
        

setup(
    name = "python-zhseg",
    version = "0.1",
    license = 'BSD',
    description = "python-zhseg is a collection of Chinese segmenting tools.",
    packages = ['zhseg'],
    package_data={'zhseg': ['data/*.dic']},
    include_package_data = True,
    zip_safe = False,
    ext_modules = [
        Extension("zhseg._mmseg", include_dirs=['mmseg-cpp'],
            sources=[
                "mmseg-cpp/algor.cpp",
                "mmseg-cpp/dict.cpp",
                "mmseg-cpp/memory.cpp",
                "mmseg-cpp/mmseg.cpp",
                "zhseg/_mmseg.cpp"
            ])
    ],
)
