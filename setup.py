#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


def long_description():
    readme = open('README.rst', encoding='utf8').read()
    return readme


setup(
    name='f',
    version='0.2.0',
    description='Ruby-Style String Interpolation for Python.',
    long_description=long_description(),
    url='https://github.com/mozillazg/f',
    author='mozillazg',
    author_email='mozillazg101@gmail.com',
    license='MIT',
    package_data={'': ['LICENSE']},
    py_modules=['f'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords='string, string interpolation',
)
