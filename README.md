# mistrust-healthcare
This repository contains the code to reproduce part of the [Racial Disparities and Mistrust in EOL Care](https://proceedings.mlr.press/v85/boag18a.html) paper and experiment with more sophisticated models (GBMs) to better account for interaction effects between variables.

## How to run
There have been substantial changes to the original code. To recreate our results, we assume that you have access to the MIMIC-III v1.4 data. Our dependencies are provided in both a requirements.txt file and an environment.yml file. You will then need to run the following notebooks:
1. create_datasets.ipynb to create some datasets to be used in the other notebooks
2. sql_queries.ipynb to create the remaining datasets used in other notebooks
3. trust.ipynb to create some mistrust models that are used in other notebooks
4. race_aggressive.ipynb to generate output graphs in the ImagesOutput/ folder
5. outcomes_ml.iypnb to run the final models (logistic regressions and GBMs) as well as perform hyperparameter tuning. The results are saved in the ModelResults/ folder. This includes both the training code and evaluation metrics code.

## Results
Note: we do not provide a copy of our pretrained models on our Github repository, but the models may be recreated by following the above steps. Our final model results from ModelResults/model_results.csv are summarized below:

| model type | task      | features                                                            | accuracy | precision | recall | f1     | auc    | sensitivity | specificity |
| ---------- | --------- | ------------------------------------------------------------------- | -------- | --------- | ------ | ------ | ------ | ----------- | ----------- |
| lr         | AMA       | age, los, insurance, gender                                         | 0.9935   | 0         | 0      | 0      | 0.8751 | 0           | 1           |
| lr         | AMA       | age, los, insurance, gender, race                                   | 0.9935   | 0         | 0      | 0      | 0.8751 | 0           | 1           |
| lr         | AMA       | age, los, insurance, gender, noncompliant                           | 0.9935   | 0         | 0      | 0      | 0.8613 | 0           | 1           |
| lr         | AMA       | age, los, insurance, gender, autopsy                                | 0.9935   | 0         | 0      | 0      | 0.875  | 0           | 1           |
| lr         | AMA       | age, los, insurance, gender, sentiment                              | 0.9935   | 0         | 0      | 0      | 0.877  | 0           | 1           |
| lr         | AMA       | age, los, insurance, gender, race, noncompliant, autopsy, sentiment | 0.9935   | 0         | 0      | 0      | 0.8615 | 0           | 1           |
| gbm        | AMA       | age, los, insurance, gender                                         | 0.9934   | 0.2322    | 0.0143 | 0.0265 | 0.8812 | 0.0143      | 0.9998      |
| gbm        | AMA       | age, los, insurance, gender, race                                   | 0.9935   | 0.6208    | 0.0289 | 0.0547 | 0.8786 | 0.0289      | 0.9999      |
| gbm        | AMA       | age, los, insurance, gender, noncompliant                           | 0.9926   | 0.1863    | 0.0247 | 0.0421 | 0.8721 | 0.0247      | 0.999       |
| gbm        | AMA       | age, los, insurance, gender, autopsy                                | 0.993    | 0.0935    | 0.0088 | 0.0159 | 0.8767 | 0.0088      | 0.9994      |
| gbm        | AMA       | age, los, insurance, gender, sentiment                              | 0.9932   | 0.2366    | 0.0174 | 0.0318 | 0.8676 | 0.0174      | 0.9996      |
| gbm        | AMA       | age, los, insurance, gender, race, noncompliant, autopsy, sentiment | 0.9924   | 0.0838    | 0.0143 | 0.0242 | 0.8692 | 0.0143      | 0.9989      |
| lr         | CS        | age, los, insurance, gender                                         | 0.8872   | 0.15      | 0.0002 | 0.0004 | 0.7087 | 0.0002      | 1           |
| lr         | CS        | age, los, insurance, gender, race                                   | 0.8872   | 0.4       | 0.0004 | 0.0009 | 0.708  | 0.0004      | 1           |
| lr         | CS        | age, los, insurance, gender, noncompliant                           | 0.887    | 0.4952    | 0.0416 | 0.0765 | 0.7058 | 0.0416      | 0.9945      |
| lr         | CS        | age, los, insurance, gender, autopsy                                | 0.8861   | 0.4603    | 0.0521 | 0.0935 | 0.7177 | 0.0521      | 0.9922      |
| lr         | CS        | age, los, insurance, gender, sentiment                              | 0.8873   | 0.6923    | 0.0028 | 0.0056 | 0.7065 | 0.0028      | 0.9998      |
| lr         | CS        | age, los, insurance, gender, race, noncompliant, autopsy, sentiment | 0.8865   | 0.4773    | 0.0592 | 0.1053 | 0.7191 | 0.0592      | 0.9917      |
| gbm        | CS        | age, los, insurance, gender                                         | 0.8874   | 0.5079    | 0.0618 | 0.1096 | 0.7511 | 0.0618      | 0.9924      |
| gbm        | CS        | age, los, insurance, gender, race                                   | 0.8877   | 0.5167    | 0.0609 | 0.1084 | 0.7512 | 0.0609      | 0.9929      |
| gbm        | CS        | age, los, insurance, gender, noncompliant                           | 0.8877   | 0.529     | 0.0458 | 0.0842 | 0.7536 | 0.0458      | 0.9948      |
| gbm        | CS        | age, los, insurance, gender, autopsy                                | 0.8875   | 0.5117    | 0.0546 | 0.0986 | 0.7613 | 0.0546      | 0.9934      |
| gbm        | CS        | age, los, insurance, gender, sentiment                              | 0.8877   | 0.5233    | 0.0593 | 0.1065 | 0.7547 | 0.0593      | 0.9931      |
| gbm        | CS        | age, los, insurance, gender, race, noncompliant, autopsy, sentiment | 0.8882   | 0.5449    | 0.0598 | 0.1077 | 0.7654 | 0.0598      | 0.9936      |
| lr         | MORTALITY | age, los, insurance, gender                                         | 0.8958   | 0         | 0      | 0      | 0.5964 | 0           | 1           |
| lr         | MORTALITY | age, los, insurance, gender, race                                   | 0.8958   | 0         | 0      | 0      | 0.6093 | 0           | 1           |
| lr         | MORTALITY | age, los, insurance, gender, noncompliant                           | 0.8958   | 0         | 0      | 0      | 0.5961 | 0           | 1           |
| lr         | MORTALITY | age, los, insurance, gender, autopsy                                | 0.8958   | 0         | 0      | 0      | 0.5991 | 0           | 1           |
| lr         | MORTALITY | age, los, insurance, gender, sentiment                              | 0.8958   | 0         | 0      | 0      | 0.5949 | 0           | 1           |
| lr         | MORTALITY | age, los, insurance, gender, race, noncompliant, autopsy, sentiment | 0.8958   | 0         | 0      | 0      | 0.6148 | 0           | 1           |
| gbm        | MORTALITY | age, los, insurance, gender                                         | 0.9008   | 0.6851    | 0.0934 | 0.1637 | 0.6921 | 0.0934      | 0.9947      |
| gbm        | MORTALITY | age, los, insurance, gender, race                                   | 0.9016   | 0.699     | 0.0986 | 0.1727 | 0.6965 | 0.0986      | 0.995       |
| gbm        | MORTALITY | age, los, insurance, gender, noncompliant                           | 0.9014   | 0.675     | 0.1037 | 0.1796 | 0.7105 | 0.1037      | 0.9942      |
| gbm        | MORTALITY | age, los, insurance, gender, autopsy                                | 0.9013   | 0.6851    | 0.0993 | 0.1733 | 0.7014 | 0.0993      | 0.9946      |
| gbm        | MORTALITY | age, los, insurance, gender, sentiment                              | 0.9014   | 0.6693    | 0.1069 | 0.1841 | 0.7265 | 0.1069      | 0.9938      |
| gbm        | MORTALITY | age, los, insurance, gender, race, noncompliant, autopsy, sentiment | 0.9028   | 0.7088    | 0.1137 | 0.1957 | 0.7579 | 0.1137      | 0.9946      |
