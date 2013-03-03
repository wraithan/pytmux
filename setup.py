#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pytmux

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

required = []

setup(
    name='pytmux',
    version=pytmux.__version__,
    description='A simple wrapper for tmux.',
    long_description=open('README.rst').read(),
    author='Wraithan (Chris McDonald)',
    author_email='xwraithanx@gmail.com',
    url='https://github.com/wraithan/pytmux',
    packages= ['pytmux'],
    install_requires=required,
    license='Apache License, Version 2.0',
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
