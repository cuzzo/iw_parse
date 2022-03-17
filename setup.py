#!/usr/bin/env python3

# Hugo Chargois - 17 Mar. 2022 - v0.0.5
# setup.py written by Kyle Krattiger (gitlab.com/mrmusic25)

# Script to allow installation with pip

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

params = {
    "scripts" : ['iw_parse/iw_parse']
}

setuptools.setup(
    name='iw_parse',
    version='0.0.5',
    description='iwlist scan for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cuzzo/iw_parse',
    author='Hugo Chargois',
    license='BSD-2-Clause',
    packages=['iw_parse'],
    classifiers=[
        'Topic :: System :: Operating System Kernels :: Linux',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    **params
)