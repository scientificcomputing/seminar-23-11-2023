---
theme: default
paginate: true
header: 'Best Practices in Modern Software Development: Documentation'
footer: '23.11.23 - Jørgen Dokken'
size: 16:9
style: |
  .small-text {
    font-size: 0.55rem;
  }
html: true
marp: true
---

# Documentation
Best Practices in Modern Software Development: 23.11.23

Jørgen Dokken


---

## What is documentation?

* Background and motivation
    - What do you try to solve?
* Instructions on how to install the software and necessary dependencies
* Instructions on how to use the software
    - Tutorials / demos
    - API documentation
* Instructions on how to get help or contribute
* https://diataxis.fr/

---

## Why do we need documentation?

* Make it easier for users (including yourself) to understand and use your code
* Make it easier for other to contribute (file issues / fix bugs)
* Which will make your software better

---

## The README file

- The first documentation a user reads is the README file
- Should include
  - Title of the project
  - Description of the project
  - Installation instructions
  - How to get started

---

- Could include
  - Badges
  - Information about how to contribute
  - License information
  - Credits
  - Example
  - How to cite
  - Screenshots / figures
- https://readme.so


---


## Using JupyterBook to create documentation

- [JupyterBook](https://jupyterbook.org/en/stable/intro.html) is a powerful framework for writing documentation
- You can use Markdown (Myst), Notebooks and pure python files in your documentation.
- It integrates well with latex (math) and Sphinx (for parsing docstrings)

---

## Add extra dependencies for docs

To use `jupyter-book` in your project you should add some extra dependencies

```yaml
[project.optional-dependencies]
docs = [
    "jupyter-book",
    "jupytext",
    "sphinxcontrib-bibtex",
]
```

---

## Compile the exact versions your use with pip-compile

Use
```
pip-compile --extra=docs --output-file=requirements-docs.txt pyproject.toml
```


---

## Need to create a config file called `_config.yml`

```yaml
# _config.yml
title: Example paper
author: Henrik Finsberg and Jørgen Dokken
copyright: "2023"
only_build_toc_files: true

parse:
  myst_enable_extensions:
    - amsmath
    - dollarmath
    - linkify


sphinx:
  config:
    nb_execution_show_tb: True
    html_theme_options:
      navigation_with_keys: false
    html_last_updated_fmt: "%b %d, %Y"
    nb_custom_formats:
        .py:
            - jupytext.reads
            - fmt: py

  extra_extensions:
  - 'sphinx.ext.autodoc'
  - 'sphinx.ext.napoleon'
  - 'sphinx.ext.viewcode'

exclude_patterns: [".pytest_cache/*", ".github/*"]
```

---

## And a table of contents called `_toc.yml`

```yaml
format: jb-book
root: README

chapters:
  - file: docs/install.md
  - file: docs/math.md
  - file: demo.py
```

---

## Building the book

Install JupyterBook
```
python3 -m pip install jupyter-book
```

Build the book (in the root where `_config.yml` amd `_toc.yml` is located).
```
jupyter-book build .
```

---

Demo `code/1-documentation-basic`

---

## Documenting code using docstrings and type hints

- There are standard ways to document your code

- We recommend to use either the Google style or Numpy style

- https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#google-vs-numpy


---

## VSCode extension to generate docstrings

https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

![w:700 center](https://github.com/NilsJPWerner/autoDocstring/raw/HEAD/images/demo.gif)

---

## Using MyST-Markdown to write content

- JupyterBook support a flavor of Markdown called *MyST*.
- Here you write so called directives
    ````
    ```{directivename}
    Content
    ```
    ````
    e.g
    ````
    ```{math}
    x^2 + y^2 = z^2
    ```
    ````

---

## MyST-markdown math

It is also possible to use MyST to labels to equations

````
```{math}
:label: my_label
w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
```
````
and then use
```
- A link to an equation directive: {eq}`my_label`
```

---

## Support `$` in math

To support `$` in math equations you need to add a myst extension to the JupyterBook config

```yaml
parse:
  myst_enable_extensions:
    - amsmath
    - dollarmath
    - linkify
```

* Here we also add `amsmath` to support amsmath LaTeX environments and linkify which will turn urls into links.

---

## More MyST features

- Create citations: https://jupyterbook.org/en/stable/tutorials/references.html#create-a-citation
- Adding images: https://jupyterbook.org/en/stable/content/figures.html
- More: https://jupyterbook.org/en/stable/content/index.html

---

## Publishing the book to GitHub pages

- Create a new file `.github/workflows/build_docs.yml` which contains a workflow for building the docs
- Also remember to go to your [repository settings on GitHub](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) to allow for GitHub pages, see

---

```yaml
# Simple workflow for deploying static content to GitHub Pages
name: Build docs

on:
  workflow_dispatch:
  workflow_call:
  pull_request:
    branches:
      - main

jobs:
  build_docs:
    runs-on: ubuntu-22.04
    env:
      PYTHON_VERSION: "3.10"
      PUBLISH_DIR: ./_build/html

    steps:
      # checkout the repository
      - uses: actions/checkout@v4

      # setup Python
      - name: Install Python ${{ env.PYTHON_VERSION }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      # preserve pip cache to speed up installation
      - name: Cache pip
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          # Look to see if there is a cache hit for the corresponding requirements file
          key: ${{ runner.os }}-pip-${{ hashFiles('*requirements-docs.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      - name: Install Python dependencies
        run: |
          python3 -m pip install --upgrade pip
          python3 -m pip install -r requirements-docs.txt

      - name: Build docs
        run: python3 -m jupyter book build .

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          name: documentation
          path: ${{ env.PUBLISH_DIR }}
          if-no-files-found: error
```

---

## Publishing the book to GitHub pages

- Create a new file `.github/workflows/publish_docs.yml` which contains a workflow for publishing the docs to github pages

---

```yaml
name: Github Pages

on:
  push:
    branches: [main]  # Only run on push to main

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow one concurrent deployment
concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  build-docs:
    uses: ./.github/workflows/build_docs.yml

  deploy:
    needs: [build-docs]

    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    runs-on: ubuntu-latest
    steps:
      - name: Download docs artifact
        # docs artifact is uploaded by build-docs job
        uses: actions/download-artifact@v3
        with:
          name: documentation
          path: "./public"

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: "./public"

      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v3

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```
