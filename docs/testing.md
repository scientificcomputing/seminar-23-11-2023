---
theme: default
paginate: true
header: 'Best Practices in Modern Software Development: Linters, formatters and pre-commit hooks'
footer: '23.11.23 - Henrik Finsberg and Jørgen Dokken'
size: 16:9
style: |
  .small-text {
    font-size: 0.55rem;
  }
html: true
marp: true
---

# Linters, formatters and pre-commit hooks
Best Practices in Modern Software Development: 23.11.23

Henrik Finsberg and Jørgen Dokken

---


## Agenda

- Linters
- Formatters
- pre-commit hooks
- Running pre-commit hooks in using GitHub actions



---

## What is a linter?

- A linter is a tool that analyses your source code and reports potential problems.

---

## Example linters

- [`flake8`](https://github.com/PyCQA/flake8): points out general problems
- [`ruff`](https://github.com/astral-sh/ruff): similar to `flake8` only more and faster (recommended). `ruff` also include features from `isort`, `pyupgrade`, `black`, ...

* You can install them with `pip` or `pipx` [FIXME: Talk about `pipx`?]

---

# Demo: linting

```python
# file.py
import math

def main():
    x = 1
    y = 2
    z = y + 2
    return z
```

* `ruff file.py`
    ```
    ruff file.py
    file.py:1:8: F401 [*] `math` imported but unused
    file.py:4:5: F841 [*] Local variable `x` is assigned to but never used
    Found 2 errors.
    [*] 2 potentially fixable with the --fix option.
    ```

---

## Ignore errors

```python
# file.py
import math  # noqa: F401

def main():
    x = 1  # noqa: F841
    y = 2
    z = y + 2
    return z
```

---

## Formatters

- Formatters are tools that will format your code to follow a certain code style
- When collaborating with others you need to agree on a code style
- [`black`](https://github.com/psf/black) should be the default choice
* It is also possible to [setup VSCode](https://code.visualstudio.com/docs/python/formatting) to format you code when you save
* It is also possible to use `ruff` for formatting (but is seems to currently be an experimental feature)

---

## Demo

Try to run black on the following code

```python
import math

def main():
    x=1# Some comment
    y = 2
    #Some other comment
    z = y +2
    a_very_long_function_with_many_arguments(first_argument=x, second_argument=y, third_argument=z)



    return z
```

---

## Static type checker

- Use `mypy` to check your types
- [`mypy`](https://mypy.readthedocs.io/en/stable/)
- Helps to catch bugs
- Will only run on code with type hints

---

# Demo: static type checking

```python
# file.py

class Person:
    def __init__(self, name: str, year_born: int) -> None:
        self.name = name
        self.year_born = year_born

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, year_born={self.year_burn})"
```

* `$ mypy file.py`
    ```
    file.py:7: error: "Person" has no attribute "year_burn"; maybe "year_born"?  [attr-defined]
    Found 1 error in 1 file (checked 1 source file)
    ```
* Ignore line by using comment `# type: ignore`

---

## Pre-commit hooks

- It is possible to set up pre-commit hooks that will run any time you commit to the repo
- There is a convenient python package called `pre-commit` that makes it easy to configure, see https://pre-commit.com
- `pip install pre-commit` (or pipx)

---

## Example configuration

Define configurations in `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-docstring-first
      - id: debug-statements
      - id: check-toml

  - repo: https://github.com/psf/black
    rev: 22.12.0
    hooks:
      - id: black

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: 'v0.0.254'
    hooks:
      - id: ruff

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.950
    hooks:
      - id: mypy
```

---

* Install hooks using
    ```
    pre-commit install
    ```

* Run all hooks on all files using
    ```
    pre-commit run --all
    ```

---

## Exercise

Install pre-commit hooks and run them on all the files in your repo

---

## Run pre-commit in CI

Add `pre-commit` as a part of your continuous integration by creating a file `.github/workflows/pre-commit.yml` with the following content

```yaml
name: pre-commit

on:
  pull_request:
  push:
    branches: [main]

jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v4
    - uses: pre-commit/action@v3.0.0
```
