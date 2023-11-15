---
theme: default
paginate: true
header: 'Best Practices in Modern Software Development: Paper with code'
footer: '23.11.23 - Henrik Finsberg and Jørgen Dokken'
size: 16:9
style: |
  .small-text {
    font-size: 0.55rem;
  }
html: true
marp: true
---


# Paper with code
Best Practices in Modern Software Development: 23.11.23

Henrik Finsberg and Jørgen Dokken


---

## Agenda

- How to set up a repo to reproduce results in a paper
    - Starting a new repository
    - Set up reproducible environment
    - Create tests to make sure results remain valid
    - Host results online via GitHub pages
    - Make sure to specify how to cite
    - Licensing

---

## Starting a new project

- Use cookiecutter
- Use template
- Copy files from existing project

---

## Demo

Example paper with pure python dependencies:

https://github.com/scientificcomputing/example-paper


---

## Demo

Example paper with dependencies in docker image

https://github.com/scientificcomputing/example-paper-fenics
