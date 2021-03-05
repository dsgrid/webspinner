# Developer How-To

To get all of the development dependencies for Python:

```
pip install webspinner[dev]
```

## Create a new release

1. Update version number, CHANGES.txt, setup.py, LICENSE and header as needed
2. Create release on github
3. Release tagged version on pypi
    
## Release on pypi

1. [using testpyi](https://packaging.python.org/guides/using-testpypi/) has good instructions for setting up your user account on TestPyPI and PyPI, and configuring twine to know how to access both repositories.
2. Test the package

    ```
    python setup.py sdist
    twine upload --repository testpypi dist/*
    # look at https://test.pypi.org/project/webspinner/
    pip install --index-url https://test.pypi.org/simple/ webspinner[aws,pgsql]
    # check it out ... fix things ...
    ```

3. Upload to pypi

    ```
    twine upload --repository pypi dist/*
    ```
