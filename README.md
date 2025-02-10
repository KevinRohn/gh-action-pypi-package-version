# :package: GitHub Action `Fetch PyPi package version`

> A GitHub Action to retrieve package version information from PyPI and TestPyPI.

## About

This action fetches the latest version and all release versions of a specified package from either PyPI or TestPyPI.

## Usage

```yml
- name: Check PyPI Package Version
  id: version_check
  uses: KevinRohn/gh-action-pypi-package-version@v1
  with:
    package-name: '<package-name>'
    endpoint: 'pypi'
```


### Usage Examples

**Check Package Version on PyPI**

```yml
- name: Check PyPI Version
  id: pypi_check
  uses: KevinRohn/gh-action-pypi-package-version@v1
  with:
    package-name: 'django'
    endpoint: 'pypi'

- name: Print Version
  run: echo "Latest version: ${{ steps.pypi_check.outputs.latest-version }}"
```

**Check Package Version on TestPyPI**

```yml
- name: Check TestPyPI Version
  id: testpypi_check
  uses: KevinRohn/gh-action-pypi-package-version@v1
  with:
    package-name: 'django'
    endpoint: 'testpypi'

- name: Print Version
  run: echo "Latest version: ${{ steps.testpypi_check.outputs.latest-version }}"
```

## Inputs

The action supports the following inputs:

- `package-name`  
  Name of the Python package to check.
  **Required:** *true*

- `endpoint`  
  Package repository to check. Options: `pypi`, `testpypi`.
  **Required:** *false*

## Outputs

- `latest-version`  
  The latest version of the package.

- `all-releases`  
  JSON array containing all release versions of the package.