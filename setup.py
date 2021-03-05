import setuptools
import pathlib

here = pathlib.Path(__file__).parent

with open(here / 'webspinner' / '_version.py', encoding='utf-8') as f:
    version = f.read()

version = version.split()[2].strip('"').strip("'")

with open(here / 'README.md', encoding='utf-8') as f:
    readme = f.read()

setuptools.setup(
    name = 'webspinner',
    version = version,
    author = 'Elaine T. Hale',
    author_email = 'elaine.hale@nrel.gov',
    packages = setuptools.find_packages(),
    url = 'https://github.com/dsgrid/webspinner',
    description = 'Python utilities for working with various dsgrid data sources',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    install_requires=[
        'sqlalchemy'
    ],
    extras_require={
        'aws': [
            'pyathena',
            'awscli'
        ],
        'pgsql': [
            'pgpasslib',
            'psycopg2'
        ],
        'parquet': [
            'pyarrow'
        ],
        'dev': [
            'twine'
        ]
    }
)
