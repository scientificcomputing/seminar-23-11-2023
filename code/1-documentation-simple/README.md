# Documentation basic

Here is an example of basic documentation with [jupyter-book](https://jupyterbook.org/) and some of the features of markdown.

We can get a breakdown of the current page by adding sub-headings by using `##` for a second level heading, and `###` for a third level heading etch

## Subheading

Here we have some more text.
We can add a block of code with 3x` syntax, i.e.
````
```python
import numpy as np
# Here is a comment
```
````
### Code example
The above code would render as
```python
import numpy as np
# Here is a comment
```

## New sub heading
You can also add more fancy things, such as a note
```{note}
This is a note
```
and warnings
```{warning}
I warn you
```
### References
We add a bibliography file `references.bib` to our repo, and cite things as
{cite}`Yogi2018`
See: [Jupyter-book: Citations](https://jupyterbook.org/en/stable/content/citations.html) for more information


## Bibliography
```{bibliography}
:style: alpha
:filter: docname in docnames
```
