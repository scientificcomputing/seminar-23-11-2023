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

```yml
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

```yml
format: jb-book
root: README

chapters:
  - file: docs/install.md
  - file: docs/math.md
  - file: demo.py
```

---

Demo `code/1-documentation-basic`

---

## Documenting code using docstrings and type hints

There is a standard way to document
