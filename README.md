Sample Module Repository
========================

This simple project is an example repo for Python projects I learned from Ken:

`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.

✨🍰✨
# RNAseqEnsemble

RNAseqEnsemble is an analytical framework collecting a few popular RNAseq analysis methods like DESeq, baySeq cuffdiff TSPM edgeR. 

## Requirements
RNAseqEnsemble was developed using Python 2.7.13. In addition to requirements specified in setup.py, RNAseqEnsemble requires installation of the following tools:

* [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)
* [GATK, version 3.7-0](https://software.broadinstitute.org/gatk/download/)
* [picard](https://broadinstitute.github.io/picard/)
* [samtools](http://www.htslib.org/download/)

## Installation
Proper function of RNAseqEnsemble requires the paths to depencies to be set.  To do this, manually set the paths in `paths.cfg` using a text editor.

After the correct paths have been set, install RNAseqEnsemble with the following command:
```
python setup.py install
```

## Usage
All of RNAseqEnsembles functions may be accessed using its command line interface. General usage is as follows:
```
RNAseqEnsemble COMMAND [OPTIONS] [ARGS]...
```
A list of commands can be found by using the following:
```
RNAseqEnsemble --help
```
Details about each command can be found by using the following:
```
RNAseqEnsemble COMMAND --help
```
See the [manual](docs/manual.md) for further usage details.

## Authors
RNAseqEnsemble was developed initially by Jianying Li.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments
This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) [Christopher Lavender](https://github.com/lavenderca/muver.git) [[Ken](http://www.kennethreitz.org/essays/repository-structure-and-python)project template.
