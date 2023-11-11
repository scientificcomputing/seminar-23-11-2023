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

* Only python dependencies?
    - Use python virtual environments
* Do you rely on packages with strong dependency on C++/Rust/C/Fortran (e.g Tensorflow)
    - Use conda
* Do you

---

## Publishing a docker image with Github actions


TBW
