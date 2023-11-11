---
theme: default
paginate: true
header: 'Code and Data repositories'
footer: 'BioAI seminar 23.11.23 - Henrik Finsberg and Jørgen Dokken'
size: 16:9
style: |
  .small-text {
    font-size: 0.55rem;
  }
html: true
marp: true
---

# Code and Data repositories
BioAI seminar 23.11.23
Henrik Finsberg and Jørgen Dokken

---

## Agenda

- Why version control systems
    - Why do we need version control systems.
    - Why it is good to track the history of a project and understand why certain decisions where made
- Setting up your first repository
    - Cookiecutters and template repositories
- What is GitHub?
    - Collaboration with other through code review
    - Pull requests process
    - Issue tracking
- Releases and tags
    - Create a release with a tags for specific version that you want to easily be able to go back to, e.g when you submit a paper or when a paper is published.
    - Creating a changelog to show what has been changed between releases.
- Data repositories and data sharing
    - How to share data. This should typically not be in a git repo, but rather on a data repository such as Zenodo.
    - How to deal with the case when it is not possible to share data (Generate synthetic data).


---

## Why version control systems?

* To keep a history of what has been changed and why
* To make it easy to go back to a previous version
* To make changes while maintaining a working version

---

## Setting up your first project

- Cookiecutters
    - Script that generate the files based on a few questions
    - https://github.com/scientificcomputing/generate-paper
    - https://github.com/scientific-python/cookie
    - https://www.cookiecutter.io/templates
- Templates
    - Copy all files from an existing repository


---

## Demo cookiecutter

```
pip install cookiecutter
cookiecutter gh:scientificcomputing/generate-paper
```

---

## What is GitHub?

* A place to host your remote repositories
* To make it easier to collaborate with others
* To keep a backup (on GitHub)
* Create repositories under your group's GitHub organization

---

## Code review process

* Open issue describing the problem. Use the issue tracker to discuss whether this needs to be solved.
* Clone (or fork) the repository
* Create a new branch (e.g `git checkout -b finsberg/fix-typo-in-readme`)
* Push your changes to this new branch
* Create a pull request, refer to the issue and continue the discussion

---

# Demo
- Create a new branch and open a pull request

---

# Exercise

- Create a new repo on GitHub (ex: <example-paper>)
- Run the cookiecutter and add all the files in a single commit
    ```
    git init  # Initialize
    git remote add origin <url>  # Add a new remote
    git add .  # Add all files
    git commit -m "Add files"  # Commit
    ```

---

- Push the code to the main branch
    ```
    git push -u origin main
    ```

- Create a new brach and make some changes to the README file
    ```
    git checkout -b edit-readme
    ```

- Push the branch and open a PR
    ```
    git push origin edit-readme
    ```

---


## Exercise (for the future)

Find a typo, mistake or a missing feature in any of the repositories under <https://github.com/orgs/scientificcomputing/repositories>, open an issue, fork the repo submit a PR.

---

## Creating releases and tags

* When you think that your code is ready it is time to create a release
* Your code should get a version number
    - `major.minor.micro` e.g `0.1.2`
    - Start with 0.0.1 and move to 1.0.0 when it is ready for users
    - Specify the version number in `pyproject.toml`
* Create a git tag once you have bumped the version
* Create a release on GitHub and write a changelog
    - It is also possible to create a tag during this step

---

## Write a changelog

* List the notable changes since the previous release
    - For the first release you don't need a changelog

* Information about changes are important for the users

* https://keepachangelog.com/en/1.0.0/

---

## Tools for managing versions and tags

- [`bump-my-version`](https://github.com/callowayproject/bump-my-version)
- [tbump](https://github.com/your-tools/tbump)
