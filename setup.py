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

required = [
    'docopt==0.6.1',
    'jsonschema==1.1.0',
]

setup(
    name='pytmux',
    version=pytmux.__version__,
    description='A simple wrapper for tmux.',
    long_description=(open('README.rst').read() + '\n\n' +
                      open('HISTORY.rst').read()),
    author='Wraithan (Chris McDonald)',
    author_email='xwraithanx@gmail.com',
    url='https://github.com/wraithan/pytmux',
    packages=['pytmux'],
    install_requires=required,
    license='Apache License, Version 2.0',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ),
    entry_points={
        'console_scripts': [
            'pytmux = pytmux.cli:main',
        ],
    },
)
