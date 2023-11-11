---
theme: default
paginate: true
header: 'Documentation'
footer: 'BioAI seminar 23.11.23 - Henrik Finsberg and Jørgen Dokken'
size: 16:9
style: |
  .small-text {
    font-size: 0.55rem;
  }
html: true
marp: true
---

# Documentation
BioAI seminar 23.11.23
Henrik Finsberg and Jørgen Dokken


---

## Agenda

- Why documentation?
- Writing docstrings and generating API documentation
    - numpy vs Google style
- Writing documentation using Jupyter-Book
- Hosting documentation on GitHub pages


---

## What is documentation?

* Background and motivation
    - What do you try to solve?
* Instructions on how to install the software
    - Installation instructions
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

## Using JupyterBook to create documentation

- [JupyterBook](https://jupyterbook.org/en/stable/intro.html) is a powerful framework for writing documentation
- You can use Markdown (Myst), Notebooks and pure python files in your documentation.
- It integrates well with latex (math) and Sphinx (for parsing docstrings)

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

- Create a new file `.github/workflows/build_docs.yml`

```yaml
# Simple workflow for deploying static content to GitHub Pages
name: Deploy static content to Pages

on: [push]


# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow one concurrent deployment
concurrency:
  group: "pages"
  cancel-in-progress: true

env:
  # Directory that will be published on github pages
  PUBLISH_DIR: ./_build/html

jobs:

  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Install dependencies
        run: |
          python3 -m pip install jupyter-book jupytext

      - name: Build docs
        run: jupyter book build .

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: ${{ env.PUBLISH_DIR }}

  # Single deploy job since we're just deploying
  deploy:
    if: github.ref == 'refs/heads/main'
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v3


      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```
