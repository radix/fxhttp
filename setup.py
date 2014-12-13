#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = 'fxhttp/_version.py'
versioneer.versionfile_build = 'fxhttp/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'fxhttp-'


with open('README.rst') as f:
    readme = f.read()

setup(
    name='fxhttp',
    version=versioneer.get_version(),
    description='HTTP Effects',
    long_description=readme,
    author='Tom Prince',
    author_email='tom.prince@twistedmatrix.com',
    url='https://github.com/tomprince/fxhttp',
    packages=[
        'fxhttp',
    ],
    include_package_data=True,
    install_requires=[
        'treq',
        'requests',
        'effect',
        'characteristic',
    ],
    license="BSD",
    zip_safe=False,
    keywords='fxhttp',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='fxhttp.tests',
    cmdclass=versioneer.get_cmdclass(),
)
