#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'xmltodict',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='postalcodes-mexico',
    version='0.2.0',
    description="Determines large parts of a Mexican postal address from its postal code (C.P.).",
    long_description=readme + '\n\n' + history,
    author="Florian Posdziech",
    author_email='hallo@flowfx.de',
    url='https://github.com/flowfx/postalcodes_mexico',
    packages=[
        'postalcodes_mexico',
    ],
    package_dir={'postalcodes_mexico':
                 'postalcodes_mexico'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords=['postal code', 'mexico', 'address',],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
