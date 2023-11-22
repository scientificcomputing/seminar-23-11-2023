---
theme: default
paginate: true
header: 'Best Practices in Modern Software Development: Code and Data repositories'
footer: '23.11.23 - Henrik Finsberg'
size: 16:9
style: |
  .small-text {
    font-size: 0.55rem;
  }
html: true
marp: true
---

# Code and Data repositories
Best Practices in Modern Software Development: 23.11.23

Henrik Finsberg

---

## Why version control systems?

* To keep a history of what has been changed and why
* To make it easy to go back to a previous version
* To make changes while maintaining a working version

![bg fit right](https://the-turing-way.netlify.app/_images/project-history.svg)
<p class="small-text">Image is used under a CC-BY 4.0 license. DOI: 10.5281/zenodo.3332807.</p>

---

## Setting up your first project

- Templates
    - Copy all files from an existing repository
    - https://github.com/scientificcomputing/example-paper
    - https://github.com/scientificcomputing/example-paper-fenics

- Cookiecutters
    - Script that generate the files based on a few questions
    - https://github.com/scientificcomputing/generate-paper
    - https://github.com/scientific-python/cookie
    - https://www.cookiecutter.io/templates

---

## Demo cookiecutter


```
python3 -m pip install cookiecutter
python3 -m cookiecutter gh:scientificcomputing/generate-paper
```
(Here you can also use [pipx](https://pypa.github.io/pipx/))

---

```
research_paper_1
├── CITATION.cff        # Info about how to cite your project
├── LICENSE             # The license
├── README.md           # What the user should read first
├── _config.yml         # Configurations for docs
├── _toc.yml            # Table of contents for docs
├── code                # Where to put your code
│   └── README.md       # Description of the code
├── cspell.config.yaml  # Dictionary for spell checker
├── data                # Where to put your data
│   └── README.md       # Description of the data
├── docker
│   └── Dockerfile      # The docker file
├── docs                # Where to put your docs
│   ├── logo.png        # Simula Logo to put in documentation
│   └── references.bib  # Where to put your references
├── environment.yml     # Conda dependencies
└── pyproject.toml      # Python metadata and dependencies
```

---

## What is GitHub?

* A place to host your remote repositories
* To make it easier to collaborate with others
* To keep a backup (on GitHub)
* Create repositories under your group's GitHub organization (this will make it easier if you are unavailable)
    - https://github.com/scientificcomputing
    - https://github.com/ComputationalPhysiology

---

## Code review process

* Open issue describing the problem. Use the issue tracker to discuss whether this needs to be solved.
* Clone (or fork) the repository
* Create a new branch (e.g `git checkout -b finsberg/fix-typo-in-readme`)
* Push your changes to this new branch
* Create a pull request, refer to the issue and continue the discussion

---

## Do you need to use branches?

If you work alone and don't work on multiple things at the same time, the it is probably OK to just work on the `main` branch

---

# Demo / Exercise

- Create a new repo on GitHub (ex: `example-paper`)
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


## Versioning

* When you think that your code is ready for external users, it is time to create your first release
* Your code should get a version number.
* Create a release when you submit your paper.
* `MAJOR.MINOR.MICRO`
* Specify the version number in `pyproject.toml`
* Semantic or Calendar based versioning

---

## Calendar based versioning

https://calver.org

- YEAR.MONTH.DAY
- YEAR.MONTH.NUMBER
- YEAR.NUMBER
- ...
- e.g 2023.11.4


---

## Semantic versioning

https://semver.org

- `major.minor.micro` e.g `0.1.2`
- Bump micro / patch: Bug fixes not affecting the API
- Bump minor: Backward compatible API additions/changes
- Bump major: Backward incompatible API changes
- Typically start with `0` major version and bump to `1` when ready for users.
---

## Publish a new release

* Bump version in `pyproject.toml`
* Create a git tag once you have bumped the version
    ```
    git tag v0.1.2
    git push --tags
    ```
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
- [`tbump`](https://github.com/your-tools/tbump)


---

## Demo / Exercise: bump the version

- Change the version of your paper
- Create a new tag and release

---

## Licenses

- What can other users do with the material in your repository?
- No license means the nobody can use, copy, distribute, or modify the work without consent from the author
* Add a file called LICENSE to your repository. Go to GitHub, click "Add file" and type the name `LICENSE` and GitHub will provide you with some options

---

## What license to choose?

- MIT: Permissive - Others can use your code in any way, and you will not be sued if the software doesn't work (recommended in most cases)
- GPL: Copyleft - derivative work must use the same license - good way to embrace open source but often problematic for commercial companies
- LGPL: Similar to GPL but software can be used under different license
- CC-BY-4.0 - Typically used for creative work (most journals use this)

https://choosealicense.com

---

## Exercise:

You want to use dolfinx:
https://github.com/FEniCS/dolfinx

What license do you need to use?

---

You can choose if you want to use GPL or LGPL.
- If you choose GPL, you need to use GPL license
- If you choose LGPL, you can choose another license

---

## Exercise:

You would like to implement a new feature in dolfinx and use it in your code:
https://github.com/FEniCS/dolfinx

What license do you need to use?
* GPL or LGPL

---




Are you allowed to copy code from a repo with MIT license into your own repo?

```
MIT License

Copyright (c) 2023 Henrik Finsberg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

Yes, but you need to copy the license in to your repo.

Example: https://github.com/ComputationalPhysiology/mps

---

## Data repositories and data sharing

- Large datasets (more than 50MB) should not be stored in your git repository
    - Git does not work well with binary files
- Instead you should store large files in a data repository
    - Use Google Drive / Dropbox / Other while developing
    - Publish Data on Zenodo when ready (Zenodo and GitHub integrates well)

---

## Other tools for data repositories

- [DVC (open-source Version Control System for Machine Learning Projects](https://dvc.org)
- [git Large File Storage](https://git-lfs.com)
- [DataLad](https://www.datalad.org)
