---
theme: default
paginate: true
header: 'Best Practices in Modern Software Development: Paper with code'
footer: '23.11.23 - Henrik Finsberg'
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

Henrik Finsberg


---


## To produce a paper we write code

* We write code to **pre-process** data
* We write code to **run simulations**
* We write code to create figures and tables (**post-processing**)

---

## You want to publish code along with your paper

The first time you can use

- cookiecutter
    - Will prompt you with some questions
    - https://github.com/scientificcomputing/generate-paper
- template
    - Will copy the template repo
    - https://github.com/scientificcomputing/example-paper

* The second time, it is OK to copy files from an old project

---

## Write a README file

The README file should contain info about

- Short description of the code / paper
- Which paper and how to cite
- How to install the dependencies
- How to reproduce the results / run the code

---


## Setting up a reproducible environment

Write a `pyproject.toml` with the dependencies you need

* Compile a `requirements.txt` with the exact versions you used when creating the results with `pip-compile` (from [`pip-tools`](https://github.com/jazzband/pip-tools))
    ```
    pip-compile --output-file=requirements.txt pyproject.toml
    ```
* Compile extra dependencies
    ```
    pip-compile --extra=docs --output-file=requirements-docs.txt pyproject.toml
    ```

---

## Publish docker image with exact dependencies

* Write a Dockerfile which clones the repo and installs the dependencies
* Build and push the image to some public registry
    - For example, you can set up a GitHub action to push a new image when you create a new release

---


## Add the code for reproducing the results

Several ways to do this:

- Add scripts for reproducing figures and tables
    - Add asserts that will raise an error if results have changed
    - Example: https://github.com/scientificcomputing/example-paper or https://github.com/scientificcomputing/example-paper-fenics
- Add notebooks and execute them as part of building docs
    - Also here you can add asserts
    - Example: https://github.com/RangamaniLabUCSD/smart

---

## Tips and tricks

- Make it possible to pass command line arguments to the scripts so that you can e.g change the path to the results or data
    - This will also make it easier if you e.g need to run the scripts on a cluster where you need to get the data from a different path
- Set up CI to run the scripts
    - Upload the artifacts after the run

---

## Handling data

* Large datasets should not be stored in git
* Data can be stored locally, dropbox or google drive during development
* Ideally you should share the data on Zenodo (https://zenodo.org) when publishing the paper. This will make sure you get a DOI for the data.
  - It is also possible to upload data with restricted data on Zenodo
* Create a script for downloading data


## Make sure to create a tag / release

A tag is a specific snapshot of your repository, and by creating a tag it makes it easy to check out that version of the code.

You should create a tag (and a release) of the code
- when you submit the paper
- when the paper is published (if there are any changes from submission)
- if there are bug fixes

* Remember to write a changelog if you make a new release with info of what has changed since the previous version.

---

## License and Citation

 Make sure that people can use your code and provide proper attribution

- License
  - Without a license, other cannot use your code without asking you first

- Citation information
  - Write a `CITATION.cff`
