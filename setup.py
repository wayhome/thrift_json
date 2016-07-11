#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'thrift'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='thrift_json',
    version='0.1.0',
    description="converter between thrift and json",
    long_description=readme + '\n\n' + history,
    author="Young King",
    author_email='yanckin@gmail.com',
    url='https://github.com/youngking/thrift_json',
    packages=[
        'thrift_json',
    ],
    package_dir={'thrift_json':
                 'thrift_json'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='thrift_json',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
