# HDX Data Science Test
This repository contains a broken script that needs to be fixed. The script contains 3 errors:

1. The function fails to run.
2. The columns of the CSV output are not organized.
3. Some records fail to be written in the output CSV file.

A successful candidate would be able to identify the source of all the errors above and will be able to fix them, making sure that the script runs successully.

## Script Objective
This script queries the [Humanitarian Data Exchange repository API](http://docs.ckan.org/) and creates a CSV file with the results of the query. We are interested in getting a table with all datasets that contain the tag "ebola". The table should contain a number of metadata fields, but every field available in the query result.

The CSV file available in this repository contains the results of a run with the broken script. The objective is to generate that file, but without the errors it currently presents. The file can be found [here](data/dataset-list.csv).

## Getting Started
The first step is to **clone** this repository -- (*do not fork!*). You will work on the solution locally. When done, you can submit the whole repository as a `ZIP` package to the evaluation team.

## Usage

If you are in an UNIX system, we recommend using the `run.sh` script as follows:

```bash
$ bash run.sh
```

Or if you would like to run it direcly using Python, you can run:

```bash
$ python code/ebola-datasets-list.py
```

Either approach above will throw an error. You'll have to debug it.
