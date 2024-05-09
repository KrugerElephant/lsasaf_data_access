## Development

It is suggested to mostly follow the already existing notebooks at [Eumetsat Train Hub](https://catalog.trainhub.eumetsat.int/).
It is suggested to stick to the following *guiding principles*

### Guiding Principles for Preparing Jupyter Notebooks
1. **Follow the literate programming paradigm by a text/code ratio of 3**
 *  evenly distribute text through the entire Jupyter Notebook to document all code cells
 *  divide workflow into shorter subsections 
2. **Use instructional design elements to improve navigation and user experience**
 *  leverage HTML/Markdown elements that serve as instructional design elements
 *  elements to use: header, navigation pane, alert boxes ( course section and prerequisites) 
 *  add introduction section and Jupyter Notebook outline with anchor links
3. **Modularize functions to follow best practices for scientific computing**
 *  imports at the beginning of Jupyter Notebook,
 *  consistent code style and formatting,
 *  using meaningful names for variables and the modularization of content
 *  modularization of repetitive code i.e. downloading, pre-processing and visualization
4. **Leverage the wider Jupyter ecosystem to make content accessible**
5. **Aim for being reproducible**
 *  machine and human-readable instructions for the data, computing environment, and dependencies are required


For any further explanations of the layout the following texts are recommended:
* [Guiding principles to Jupyter Notebook](https://www.mdpi.com/2072-4292/14/14/3359)
* [Best practices for Collaboration with Jupyter Notebook](https://arxiv.org/pdf/2202.07233.pdf)
* [Benefits of Jupyter Notebook in the classroom](https://sci-hub.st/10.1145/3368308.3415397)

---

### Clear the Jupyter Notebook Output while using `Git`

Since the output of Jupyter Notebook cells is often some graphics that change often it is not advisable to track that with git while developing.
However, outputs can be added at the end of the development cycle. 
There are some options how to delete output cells
 1. Inside the Jupyter lab under view choose without output and save the file like that before committing.

 2. Make a **pre-commit hook** that parses the output of a cell out.
```
conda install -c conda-forge pre-commit

```
To list all available commands type **pre-commit help**.
To get pre-commit hook sample type:
```
pre-commit sample-config > .pre-commit-config.yaml
```
Modify the file according to your desired actions that will happen at the time of committing.
For the purpose of pre-commit hooks
```
# this is .pre-commit-config.yaml

repos:
- repo: https://github.com/kynan/nbstripout
  rev: 0.6.1
  hooks:
    - id: nbstripout
```

Install pre-commit 
```
pre-commit install
```
Inside .pre-commit-config.yaml we specified `nbstripout` that needs to be installed
```
conda  install -c conda-forge nbstripout
```

After running the commit it will execute tests defined in pre-commit-config.yaml for us i.e. nbstripout
If it has to delete the output it modifies the staged file and the user has to add and commit again.
To ignore the hook `--no-verify` flag is added.

```
git commit -am '' --no-verify
```

In case of many tests excluding just one can be done with
```
SKIP=nbstripout git commit -m ''
```
