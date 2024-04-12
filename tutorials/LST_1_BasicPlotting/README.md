# LST

## MLST Plot `NetCDF4` data
This Jupyter Notebook presents opening and plotting LSA SAF MLST products in `NetCDF4` file format. LSA SAF MLST product for the August 21, 2023, is Plotted in Plate-Carree and Robinson geographical projection.

## MLST Data Quality
This Jupyter Notebook presents the investigation of the LSA SAF MLST product's standard error and quality flag estimates. LSA SAF MLST product standard error and quality flag are plotted for August 21, 2023, in Lambert conformal geostationary projection.

## Description
Following the template_nb.ipynb is encouraged to be used for further presentations of Jupyter notebooks (NB) in the Eumetsat style.
Additional refinements are welcome.

## Environment Requirements
[Jupyter Notebook](https://jupyter.org) is an open-source application that allows you to create documents that include live code, equations, visualizations, and narrative text. Jupyter Notebooks presented here require `Python` as well as [`Jupyter`](https://jupyter.org/) or [`Jupyter-lab`](https://jupyter.org/) and several other `Python` libraries listed in the `Environment.yaml`.

There are multiple ways to achieve this. If no other option is preferred, we suggest the installation of the [conda](https://docs.conda.io/projects/conda/en/stable/index.html), since it works on various platforms (Linux, Windows, macOS). To install conda and set up a virtual environment:

* [1. - Download and install conda](https://docs.conda.io/projects/conda/en/stable/index.html)
* [2. - Once in `conda` create a virtual environment from the `environment.yaml` file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
```
conda env create -f evnironment_v1.yml
```
`Jupyter` is already included in `environment_v1.yaml` so no other actions are needed.

## Usage of the Jupyter Notebooks
Jupyter notebooks are a set of markdown and code cells. To use them follow the next steps:

* [1. - If using conda activate virtual environment first](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment).
```
conda activate environment_v1
```

* [2. - Run `jupyter notebook` or `jupyter lab`](https://docs.jupyter.org/en/latest/running.html) from the directory with the notebook:
```
jupyter notebook <name-of-notebook.ipynb>
```
or:
```
jupyter-lab
```
The `jupyter-lab` offers some additional tools and features for working with notebooks.

* [3. - Basic use of Jupyter Notebooks editor and basic commands is described here](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html).

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

After running the commit it will execute tests defined in pre-commit-config.yaml for us i.e nbstripout
If it has to delete the output it modifies the staged file and the user has to add and commit again.
To ignore the hook `--no-verify` flag is added.

```
git commit -am '' --no-verify
```

In case of many tests excluding just one can be done with
```
SKIP=nbstripout git commit -m ''
```


## Authors and Acknowledgment
ARSO team:
Vid Primožič,
Ahac Pazlar,
Boštjan Muri,

