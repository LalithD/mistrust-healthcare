# mistrust-healthcare
This repository contains the code to reproduce part of the [Racial Disparities and Mistrust in EOL Care](https://proceedings.mlr.press/v85/boag18a.html) paper and experiment with more sophisticated models.

## How to run
There have been substantial changes to the original code. To recreate our results, we assume that you have access to the MIMIC-III data. Our dependencies are provided in both a requirements.txt file and an environment.yml file. You will then need to run the following notebooks:
1. create_datasets.ipynb to create the datasets used in the other notebooks
2. trust.ipynb to create some models used in other notebooks
3. TBD