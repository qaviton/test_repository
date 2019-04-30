#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" updating pip version:
    ---------------------

1) increase test_step_parser.version.__version__

2) make sure these are installed:
    pip install wheel
    python setup.py bdist_wheel --universal
    pip install twine

3) run these:
    python setup.py sdist
    python setup.py bdist_wheel
    twine upload dist/*
"""


import io
from tests import __version__ as version
from setuptools import setup, find_packages


packages = []
for package in find_packages():
    if package.startswith('tests'):
        packages.append(package)


with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()


setup(
    name='functional_web_tests',
    version=version,
    description='this project is intended to provide an open source repository '
                'of automated functional web tests to help testers '
                'with repeating and similar scenarios to test and maintain '
                'a generic collection of tests intended to be copied '
                'into other testing projects or to be used for examples to these projects.',
    long_description=readme,
    keywords=['functional_web_tests'],
    author='Yehonadav Bar Elan',
    author_email='yehonadav@Qaviton.com',
    url='https://qaviton.com/',
    packages=packages,
    data_files=[('tests', ['tests/steps.json'])],
    include_package_data=True,
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    install_requires=[
        'qaviton>=0.1.1'
    ]
)
