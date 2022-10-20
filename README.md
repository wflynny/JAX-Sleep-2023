# JAX Sleep AD Workshop, 2022

This repo accompanies the Single Cell and Spatial Analysis workshop for the JAX
_Impacts of Sleep and Circadian Biology on Alzheimer’s Disease and Aging_
course in October 2022.

## How to Use

In your virtual machines, there will already be data available under
`Documents\singlecell-spatial`.  To incorporate these slides and analysis
notebooks, type (or copy-paste) the following into an Anaconda powershell prompt
```
cd C:\Users\protwiz\Documents\singlecell-spatial
conda activate sc-spatial
git init
git remote add origin https://github.com/wflynny/JAX-Sleep-AD-2020.git
git pull origin gh-pages
```

Alternatively, you can open a `Jupyter Notebook (sc-spatial)` (it's pinned on
the start menu). Once it opens in your browser:
- Select "New" from the top right corner of the screen, then "Terminal" from
  that menu.
- Copy-paste the following:
```
cd singlecell-spatial
git init
git remote add origin https://github.com/wflynny/JAX-Sleep-AD-2020.git
git pull origin gh-pages
```

From there you should be all set to navigate to the
`singlecell-spatial\workshop` folder on your Windows VM.

### Not using a windows PC?
- Data paths and loading data *should be* OS-agnostic.
- You will need the following python packages:
```
conda install -c conda-forge \
    scanpy
    squidpy
    matplotlib
    seaborn
    skimage
    jupyter
    tdqm
python -m pip install pybiomart
```
- You will need to download the data directly from the various sources listed
  at the top of each workshop notebook.

## Slides in your browser

Find the slides live at:

[wflynny.github.io/JAX-Sleep-AD-2020/](https://wflynny.github.io/JAX-Sleep-AD-2020/index.slides.html)

or locally by opening `slides.html` or `index.slides.html`.

If you want to print the slides, you can visit [this page](https://wflynny.github.io/JAX-Sleep-AD-2020/?print-pdf)


