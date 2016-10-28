#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='affinity_pdbdataset',
    version='0.1.0',
    description="To be updated",
    long_description=readme + '\n\n' + history,
    author="WY",
    author_email='panzer.wy@gmail.com',
    url='https://github.com/Reimilia/affinity_pdbdataset',
    packages=[
        'affinity_pdbdataset',
    ],
    package_dir={'affinity_pdbdataset':
                 'affinity_pdbdataset'},
    entry_points={
        'console_scripts': [
            'affinity_pdbdataset=affinity_pdbdataset.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='affinity_pdbdataset',
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
