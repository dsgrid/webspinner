from distutils.core import setup
import setuptools
import pathlib
import os

here = pathlib.Path(__file__).parent

with open(os.path.join(here, 'webspinner', '_version.py'), encoding='utf-8') as f:
    version = f.read()

version = version.split()[2].strip('"').strip("'")

setup(
    name = 'webspinner',
    version = version,
    author = 'Elaine T. Hale',
    author_email = 'elaine.hale@nrel.gov',
    packages = setuptools.find_packages(),
    url = 'https://github.com/dsgrid/webspinner',
    description = 'Python utilities for working with various dsgrid data sources',
    long_description = open('README.txt').read(),
    install_requires = open('requirements.txt').read()
)
