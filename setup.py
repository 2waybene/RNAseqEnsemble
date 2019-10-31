# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py
# I would like to thank	Kenneth 

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='RNAseqEnsemble',
    version='0.1.0',
    description='My package a collection of analysis for RNAseq experiment',
    long_description=readme,
    author='Jianying Li',
    author_email='jianying.li@google.com',
    url='https://github.com/2waybene/RNAseqEnsemble',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

