# -*- coding: utf-8 -*-
"""Installer for the cpskin.cirkwi package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read() +
    '\n' +
    'Contributors\n' +
    '============\n' +
    '\n' +
    open('CONTRIBUTORS.rst').read() +
    '\n' +
    open('CHANGES.rst').read() +
    '\n')


setup(
    name='cpskin.cirkwi',
    version='1.0.3.dev0',
    description="New product with a specific view for cirkwi - http://outil.cirkwi.com",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='boulch',
    author_email='christophe.boulanger@imio.be',
    url='https://pypi.python.org/pypi/cpskin.cirkwi',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['cpskin'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    #    'cpskin.locales',
    #    'cpskin.core',
    install_requires=[
        'plone.api',
        'plone.app.dexterity',
        'plone',
        'setuptools',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
