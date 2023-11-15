---
theme: default
paginate: true
header: 'Reproducible environments'
footer: 'BioAI seminar 23.11.23 - Henrik Finsberg and Jørgen Dokken'
size: 16:9
style: |
  .small-text {
    font-size: 0.55rem;
  }
html: true
marp: true
---

# Reproducible environments
BioAI seminar 23.11.23
Henrik Finsberg and Jørgen Dokken

---

## Agenda

- What is a development environment
- Virtual environments in python
    - pinning dependencies with `pip-tools`
    - pyproject.toml
- Conda
- Docker

---

## What is a development environment?

* An environment where you install your software in isolation from your system. Why?
    * Conflicting dependency versions
    * Easier to upgrade
    * Easier to dispose and start for scratch
    * You should always use a virtual environment!

* Three options
    - python virtual environments
    - `conda` environments
    - Docker

---

# Python virtual environments

- Python comes with a built-in library for creating virtual environments

    ```
    python3 -m venv venv
    ```
    This will create a folder called `venv` containing your virtual environment

* Activate virtual environment
    ```
    . ./venv/bin/activate
    ```

---

* Now you can install the dependencies you need
    ```
    python3 -m pip install pandas
    ```

* To deactivate your virtual environment you simply type
    ```
    deactivate
    ```

---

Demo - creating a virtual environment


---

## Exercise

Create two different virtual environments called `venv1` and `venv2`, one where you install the latest version of pandas and one where you install pandas version lower than 2.0
Verify the version using
```
python3 -c "import pandas; print(pandas.__version__)"
```

---

```
python3 -m venv venv1
. venv1/bin/activate
python3 -m pip install pandas
deactivate
python3 -m venv venv2
. venv2/bin/activate
python3 -m pip install "pandas<2.0"
deactivate
```


---

## Creating a `pyproject.toml`

- `pyproject.toml` is the recommended way to specify project metadata
- Minimum metadata
    - name
    - authors
    - license
    - version
    - dependencies

---

## Example `pyproject.toml`

FIXME: No we need build-system?

```toml
[build-system]  # Setuptools + editable install
requires = ["setuptools>=61.2"]
build-backend = "setuptools.build_meta"


[project]
name = "my-paper"
version = "0.1.0"
dependencies = [
    "matplotlib",
    "numpy",
    "scipy",
]
```

---

## Exercise

- Add `numpy`, `scipy` and `matplotlib` as dependencies in your `pyproject.toml`
- Try to install these dependencies in your virtual environment by typing
    ```
    python3 -m pip install -e .
    ```

---

## Pinning the exact versions of the libraries you use

* To ensure reproducible results, it is important that you specify the exact versions of the libraries you used
* We can use a tool called `pip-compile` (install with `pip install pip-tools`) to pin all the versions based on your `pyproject.toml`
* Use
    ```
    pip-compile --output-file=requirements.txt pyproject.toml
    ```
    to create a file `requirements.txt` containing all packages you use
* You can now install the exact dependencies using the command
    ```
    python3 -m pip install -r requirements.txt
    ```

---

## Exercise

- You want to use numpy version `1.21.5` for your project. Specify this in your `pyproject.toml` and compile the exact requirements


---

## Extra dependencies for development

* You might want to use some other libraries when developing the software (such as `pip-tools`)
* These libraries should not be required when installing the software, but it is nice for other developer to have an easy way to install these.
* You can list these in `pyproject.toml` under `project.optional-dependencies`


---

## Specifying optional dependencies in `pyproject.toml`

```yaml
[project.optional-dependencies]
test = [
    "pytest",
    "pytest-cov",
]
dev = [
    "pdbpp",
    "ipython",
    "bump-my-version",
    "pre-commit",
    "pip-tools",
]
all = [
   "my-paper[test,dev]"
]
```

---

## Installing optional dependencies

* Use
    ```
    python3 -m pip install ".[dev]"
    ```
    to install optional dependencies.
* To install several optional dependencies you can separate the names with comma
    ```
    python3 -m pip install ".[dev,test]"
    ```

---

## Pinning optional dependencies

It might be beneficial to pin your optional dependencies. This can be done using e.g

```
pip-compile --extra=dev --output-file=requirements-dev.txt pyproject.toml
```

* Here we save these dependencies to a different file called `requirements-dev.txt`, which can be installed using
    ```
    python3 -m pip install -r requirements-dev.txt
    ```

---


## Conda

TBW

---

Demo

---

## Docker

[Docker](https://www.docker.com/get-started/) is a platform that packages an application and all its dependencies together in the form of containers.

* The user needs to pull and image from a remote registry, create a container (an instance of an image)
* The user runs the code inside the container

---

## Basic docker commands

* Pull image
    ```
    docker pull <image name>
    ```
    e.g
    ```
    docker pull ghcr.io/scientificcomputing/fenics:2023-08-14
    ```

* Start new container (set working directory to `home/shared` and share this directory with your current working directory)
    ```
    docker run --name=my-research-code -w /home/shared -v $PWD:/home/shared -it ghcr.io/scientificcomputing/fenics:2023-08-14
    ```

---

* Exit container with `Ctrl+D` or `exit`
* Start existing container
    ```
    docker start my-research-code
    ```
* Stop running container
    ```
    docker stop my-research-code
    ```

* Remove existing container
    ```
    docker rm my-research-code
    ```

---

* Execute existing container
    ```
    docker exec -it my-research-code bash
    ```
* List images
    ```
    docker images
    ```
* List containers (omit `-a` to only list running containers)
    ```
    docker ps -a
    ```

---

## Demo

Running a fenics demo inside a docker container and output a file to open in Paraview
<https://fenicsproject.org/olddocs/dolfin/2019.1.0/python/demos/hyperelasticity/demo_hyperelasticity.py.html>


---

## Running jupyter inside docker

TBW

---

## Docker development workflow

* The developer needs to write a `Dockerfile` with instructions on how to build and install the dependencies
* The developer needs to build an image and push this to a registry

---


![bg right:60% fit](https://cdn.shortpixel.ai/spai/q_glossy+w_1456+h_503+to_auto+ret_img/linuxiac.com/wp-content/uploads/2021/06/what-is-docker-container.png)
<p class="small-text">Taken from https://linuxiac.com/what-is-docker-container/</p>

---

## Dockerfile

* Use some

```
FROM ghcr.io/scientificcomputing/fenics:2023-08-14

WORKDIR /repo

# Copy pyproject.toml first so that we done need to reinstall in case another file
# is changing after rebuilding docker image
RUN git clone --branch ${REPO_BRANCH} --single-branch https://github.com/scientificcomputing/example-paper-fenics.git
RUN cd example-paper-fenics && python3 -m pip install pip --upgrade && python3 -m pip install --no-cache-dir -r requirements.txt && rm -rf /tmp
```

---

## We maintain some docker images for scientific computing

https://github.com/orgs/scientificcomputing/packages


---

## What do choose?

* Use python virtual environments if you
    - have only python dependencies

* Use conda if
    - you rely on packages with strong dependency on C++/Rust/C/Fortran (e.g Tensorflow)
    - all packages exist on conda (conda-forge / bioconda)

* Use docker if you
    - need full control over the environment,
    - require additional packages that are hard to install
    - need the development version of a dependency (that is not pure python e.g FEniCS)

---

## Publishing a docker image with Github actions

The simplest way to ensure that users than exactly reproduce your environment is to use the same docker image as you

Therefore you should always publish a docker image containing the exact dependencies for reproducing the results

The templates contains a workflow for building docker images using GitHub actions for every new tag

---
