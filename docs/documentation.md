---
theme: default
paginate: true
header: "Best Practices in Modern Software Development: Documentation"
footer: "23.11.23 - Jørgen Dokken"
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

<div style="display:contents;" data-marpit-fragment>

- Background and motivation
  - What do problem are you trying to solve in this repository to solve?

</div>

<div style="display:contents;" data-marpit-fragment>

- Instructions on how to install the software and necessary dependencies
- Instructions on how to use the software
  - Tutorials / demos
  - API documentation
  
- Instructions on how to get help or contribute
</div> <div style="display:contents;" data-marpit-fragment>

- Guide to write tutorials: https://diataxis.fr/
</div>

---

## Why do we need documentation?

<div style="display:contents;" data-marpit-fragment>

- Make it easier for users (including yourself) to understand and use your code
- Make it easier for other to contribute (file issues / fix bugs)

</div>

---

## The README file

- The first documentation a user reads is the README file
- Should include
  - Title of the project
  - Description of the project
  - Installation instructions
  - How to get started

---

## The README file (continued)

- ### Optional
  - Badges
  - Information about how to contribute
  - License information
  - Credits
  - Example
  - How to cite
  - Screenshots / figures
* README skeleton generator: https://readme.so

---

## Using JupyterBook to create documentation

- [JupyterBook](https://jupyterbook.org/en/stable/intro.html) is a powerful framework for writing documentation
* You can use Markdown (Myst), Notebooks and pure Python files in your documentation.
* It integrates well with LaTeX (math) and Sphinx (for parsing docstrings)

---

## Add extra dependencies to `pyproject.toml` for docs

To use `jupyter-book` in your project you should add some extra dependencies

```yaml
[project.optional-dependencies]
docs = [
    "jupyter-book",
    "jupytext",
    "sphinxcontrib-bibtex",
    "docutils==0.17.1"
    # Temporary pin due to https://sourceforge.net/p/docutils/patches/195/
]
```

---

## Compile the exact versions your use with pip-compile

Use

```
pip-compile --extra=docs --output-file=requirements-docs.txt pyproject.toml
```

---

## Documentation configuration (`_config.yml`)
### Required info
```yaml
title: Example paper
author: Henrik Finsberg and Jørgen Dokken
copyright: "2023"
bibtex_bibfiles: "references.bib"
```

---

## Documentation configuration (`_config.yml`)
**Recommended configuration**
```yaml
only_build_toc_files: true
exclude_patterns: [".pytest_cache/*", ".github/*"]
parse:
  myst_enable_extensions:
    - amsmath
    - dollarmath
    - linkify
sphinx:
  config:
    bibtex_reference_style: author_year
    nb_execution_show_tb: True
    html_theme_options:
      navigation_with_keys: false
    html_last_updated_fmt: "%b %d, %Y"
    nb_custom_formats:
        .py:
            - jupytext.reads
            - fmt: py
```

---

## And a table of contents (`_toc.yml`)

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
<div style="display:contents;" data-marpit-fragment>

Build the book (in the root where `_config.yml` amd `_toc.yml` is located).
```
jupyter-book build .
```
<div/>

---

Demo `code/1-documentation-basic`

---

## Using MyST-Markdown to write content

- JupyterBook support a flavor of Markdown called _MyST_.
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

* Create citations: https://jupyterbook.org/en/stable/tutorials/references.html#create-a-citation
* Adding images: https://jupyterbook.org/en/stable/content/figures.html
* More: https://jupyterbook.org/en/stable/content/index.html

---

## Publishing the book to GitHub pages

- Create a new file `.github/workflows/build_docs.yml` which contains a workflow for building the docs
- Also remember to go to your [repository settings on GitHub](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) to allow for GitHub pages

---

### Example workflow
```yaml
name: Build docs
on:
  push:
    branches: "main"
jobs:
  build_docs:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install Python dependencies
        run: |
          python3 -m pip install --upgrade pip
          python3 -m pip install -r requirements-docs.txt

      - name: Build docs
        run: python3 -m jupyter book build .

      - uses: actions/upload-artifact@v3
        with:
          name: documentation
          path: ./_build/html
          if-no-files-found: error
```
---

### Publishing the book to GitHub pages

- Create a new file `.github/workflows/publish_docs.yml` which contains a workflow for publishing the docs to github pages

---

### Deploying the book
```yaml
name: Github Pages
on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

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
      - name: Download docs artifact from build-docs
        uses: actions/download-artifact@v3
        with:
          name: documentation
          path: "./public"

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: "./public"

      - uses: actions/configure-pages@v3

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

---
## API documentation

- Jupyter-book supports auto-documentation features from Sphinx.
- More information at: https://jupyterbook.org/en/stable/advanced/developers.html?highlight=api#developer-workflows

---

## Documenting code using docstrings and type hints

- There are standard ways to document your code

- We recommend to use either the Google style or Numpy style

  - https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#google-vs-numpy

---

## VSCode extension to generate docstrings

https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

![w:700 center](https://github.com/NilsJPWerner/autoDocstring/raw/HEAD/images/demo.gif)
