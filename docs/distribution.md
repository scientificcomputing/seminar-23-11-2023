---
theme: default
paginate: true
header: 'Best Practices in Modern Software Development: Distribution'
footer: '23.11.23 - Henrik Finsberg and Jørgen Dokken'
size: 16:9
style: |
  .small-text {
    font-size: 0.55rem;
  }
html: true
marp: true
---

# Distribution
Best Practices in Modern Software Development: 23.11.23

Henrik Finsberg and Jørgen Dokken

---

## Agenda

- How to package a python project
- Uploading a package to pypi
    - Creating a GitHub action to publish a package on pypi whenever you make a new release
- Uploading conda package to conda-forge
- Creating and publishing docker images
    - Creating a GitHub action to publish a new docker image to the GitHub registry whenever you make a new release
- Licensing
    - Which license to put on your code and why you should use a permissive license

---

## Creating a package

- A set of modules can be collected in a package

- A package is organized as module files in a directory tree

- Each subdirectory must have a __init__.py file (can be empty)

```
examples/my-package
├── LICENSE
├── pyproject.toml
├── README.md
├── src
│   └── pkg
│       ├── analysis.py
│       ├── __init__.py
│       └── printing
│           ├── __init__.py
│           └── printing.py
└── test
    ├── test_analysis.py
    └── test_printing.py
```

---

## Installing a package
