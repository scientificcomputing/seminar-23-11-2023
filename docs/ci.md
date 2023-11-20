---
theme: default
paginate: true
header: 'Continuous Integration'
footer: '23.11.23 - Henrik Finsberg and Jørgen Dokken'
size: 16:9
style: |
  .small-text {
    font-size: 0.55rem;
  }
html: true
marp: true
---


<!-- As your research evolves from ideas into code, you would like to ensure that the code can be used by others.
To ensure quality, consistency and reproducibility of your research, -->

# Continuous Integration
<center><img src="https://i.redd.it/6u77tkmyaomz.jpg" alt="works on my machine" class="bg-primary" width="400px">

Source: [Reddit - Programmer Humor - Works on my Machine](https://www.reddit.com/r/ProgrammerHumor/comments/70we66/it_works_on_my_machine/)

---

## How to start?

* Many ways to do CI; use the one you prefer
  - Github Actions
  - Azure DevOps
  - Circle CI
  - Travis
  - List of [CI-services](https://github.com/ligurio/awesome-ci)
* We will use Github Actions

---

## Create a workflow

* Create folder `.github/workflows`
* Add a `name_of_workflow.yml`

---

## When should the workflow be executed?

name: Build documentation and upload artifact
```yaml
on:
  pull_request:
    branches: main
  push:
    branches:
      - "*"
    tags:
      - "v*"
  workflow_call:
  workflow_dispatch:
```

---

### Run on pull-request
```yaml
on:
  pull_request:
    branches: main
```
* Workflow is triggered whenever a pull request is made against the main branch
* Can make a list of branches, or include all (`"*"`, or no branch `"!*"` or patterns `"v*"``)

---


---
