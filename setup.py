#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(matthewturk): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='dispersing',
    version='0.1.0',
    description="A game asset extractor for The Summoning",
    long_description=readme + '\n\n' + history,
    author="Matthew Turk",
    author_email='matthewturk@gmail.com',
    url='https://github.com/matthewturk/dispersing',
    packages=find_packages(include=['dispersing']),
    entry_points={
        'console_scripts': [
            'dispersing=dispersing.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='dispersing',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
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
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
