#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit egp_plot/__version__.py
version = {}
with open(os.path.join(here, 'egp', 'plot', '__version__.py')) as f:
    exec(f.read(), version)

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='egp_plot',
    version=version['__version__'],
    description="My collection of Python plotting functions",
    long_description=readme + '\n\n',
    author="E. G. Patrick Bos",
    author_email='p.bos@esciencecenter.nl',
    url='https://github.com/egpbos/egp_plot',
    packages=[
        'egp_plot',
    ],
    package_dir={'egp_plot':
                 'egp/plot'},
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='egp_plot',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    install_requires=[
        'matplotlib'
    ],
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'sphinx_rtd_theme',
        'recommonmark'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pycodestyle',
    ],
    extras_require={
        'dev':  ['prospector[with_pyroma]', 'yapf', 'isort'],
    }
)
