# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_markers: '"""'
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.5.1
#   kernelspec:
#     display_name: P4_plagiarism_detection
#     language: python
#     name: p4_plagiarism_detection
# ---

# %%
import json
import os
import re
from typing import Tuple

import boto3
import numpy as np
import pandas as pd
import sagemaker
from botocore.exceptions import ClientError
from deepdiff import DeepHash
from dotenv import load_dotenv
from sagemaker.sklearn import SKLearn
from sklearn.metrics import accuracy_score

from helpers import OUTPUT_DIR, S3_FEATURE_DIR, S3_MODEL_DIR

load_dotenv(override=True)

# session and role
sagemaker_session = sagemaker.Session()
role = os.environ.get('SAGEMAKER_EXECUTION_ROLE') or sagemaker.get_execution_role()

# create an S3 bucket
bucket = sagemaker_session.default_bucket()

# these are the largest training / deploy instances available in aws educate
TRAIN_INSTANCE = 'ml.m5.large'
DEPLOY_INSTANCE = 'ml.m5.large'

# %% [markdown]
"""
# Plagiarism Detection Model

Now that you've created training and test data, you are ready to define and train a model. Your goal in this notebook, will be to train a binary classification model that learns to label an answer file as either plagiarized or not, based on the features you provide the model.

This task will be broken down into a few discrete steps:

* Upload your data to S3.
* Define a binary classification model and a training script.
* Train your model and deploy it.
* Evaluate your deployed classifier and answer some questions about your approach.

To complete this notebook, you'll have to complete all given exercises and answer all the questions in this notebook.
> All your tasks will be clearly labeled **EXERCISE** and questions as **QUESTION**.

It will be up to you to explore different classification models and decide on a model that gives you the best performance for this dataset.

---
"""

# %% [markdown]
"""
## Load Data to S3

In the last notebook, you should have created two files: a `training.csv` and `test.csv` file with the features and class labels for the given corpus of plagiarized/non-plagiarized text data.

>The below cells load in some AWS SageMaker libraries and creates a default bucket. After creating this bucket, you can upload your locally stored data to S3.

Save your train and test `.csv` feature files, locally. To do this you can run the second notebook "2_Plagiarism_Feature_Engineering" in SageMaker or you can manually upload your files to this notebook using the upload icon in Jupyter Lab. Then you can upload local files to S3 by using `sagemaker_session.upload_data` and pointing directly to where the training data is saved.
"""

# %%
"""
DON'T MODIFY ANYTHING IN THIS CELL THAT IS BELOW THIS LINE
"""
# Moved to top for easier execution while iterating on notebook

# %% [markdown]
"""
## EXERCISE: Upload your training data to S3

Specify the `data_dir` where you've saved your `train.csv` file. Decide on a descriptive `prefix` that defines where your data will be uploaded in the default S3 bucket. Finally, create a pointer to your training data by calling `sagemaker_session.upload_data` and passing in the required parameters. It may help to look at the [Session documentation](https://sagemaker.readthedocs.io/en/stable/session.html#sagemaker.session.Session.upload_data) or previous SageMaker code examples.

You are expected to upload your entire directory. Later, the training script will only access the `train.csv` file.
"""

# %%
# should be the name of directory you created to save your features data

data_to_try = ['all-features']
prefix = None
data_desc = None

for data_desc in data_to_try:
    # set prefix, a descriptive name for a directory
    prefix = S3_FEATURE_DIR / data_desc

    # upload all data to S3
    sagemaker_session.upload_data(path=str(OUTPUT_DIR / data_desc), key_prefix=prefix)


# %% [markdown]
"""
### Test cell

Test that your data has been successfully uploaded. The below cell prints out the items in your S3 bucket and will throw an error if it is empty. You should see the contents of your `data_dir` and perhaps some checkpoints. If you see any other files listed, then you may have some old model files that you can delete via the S3 console (though, additional files shouldn't affect the performance of model developed in this notebook).
"""

# %%
"""
DON'T MODIFY ANYTHING IN THIS CELL THAT IS BELOW THIS LINE
"""
# confirm that data is in S3 bucket
empty_check = []
for obj in boto3.resource('s3').Bucket(bucket).objects.filter(Prefix=str(prefix)):
    empty_check.append(obj.key)
    print(obj.key)

assert len(empty_check) != 0, 'S3 bucket is empty.'
print('Test passed!')

# %% [markdown]
"""
---

# Modeling

Now that you've uploaded your training data, it's time to define and train a model!

The type of model you create is up to you. For a binary classification task, you can choose to go one of three routes:
* Use a built-in classification algorithm, like LinearLearner.
* Define a custom Scikit-learn classifier, a comparison of models can be found [here](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html).
* Define a custom PyTorch neural network classifier.

It will be up to you to test out a variety of models and choose the best one. Your project will be graded on the accuracy of your final model.

---

## EXERCISE: Complete a training script

To implement a custom classifier, you'll need to complete a `train.py` script. You've been given the folders `source_sklearn` and `source_pytorch` which hold starting code for a custom Scikit-learn model and a PyTorch model, respectively. Each directory has a `train.py` training script. To complete this project **you only need to complete one of these scripts**; the script that is responsible for training your final model.

A typical training script:
* Loads training data from a specified directory
* Parses any training & model hyperparameters (ex. nodes in a neural network, training epochs, etc.)
* Instantiates a model of your design, with any specified hyperparams
* Trains that model
* Finally, saves the model so that it can be hosted/deployed, later

### Defining and training a model
Much of the training script code is provided for you. Almost all of your work will be done in the `if __name__ == '__main__':` section. To complete a `train.py` file, you will:
1. Import any extra libraries you need
2. Define any additional model training hyperparameters using `parser.add_argument`
2. Define a model in the `if __name__ == '__main__':` section
3. Train the model in that same section

Below, you can use `!pygmentize` to display an existing `train.py` file. Read through the code; all of your tasks are marked with `TODO` comments.

**Note: If you choose to create a custom PyTorch model, you will be responsible for defining the model in the `model.py` file,** and a `predict.py` file is provided. If you choose to use Scikit-learn, you only need a `train.py` file; you may import a classifier from the `sklearn` library.
"""

# %%
# directory can be changed to: source_sklearn or source_pytorch
# !pygmentize sagemaker_container/train_and_deploy.py

# %% [markdown]
"""
### Provided code

If you read the code above, you can see that the starter code includes a few things:
* Model loading (`model_fn`) and saving code
* Getting SageMaker's default hyperparameters
* Loading the training data by name, `train.csv` and extracting the features and labels, `train_x`, and `train_y`

If you'd like to read more about model saving with [joblib for sklearn](https://scikit-learn.org/stable/modules/model_persistence.html) or with [torch.save](https://pytorch.org/tutorials/beginner/saving_loading_models.html), click on the provided links.
"""

# %% [markdown]
"""
---
# Create an Estimator

When a custom model is constructed in SageMaker, an entry point must be specified. This is the Python file which will be executed when the model is trained; the `train.py` function you specified above. To run a custom training script in SageMaker, construct an estimator, and fill in the appropriate constructor arguments:

* **entry_point**: The path to the Python script SageMaker runs for training and prediction.
* **source_dir**: The path to the training script directory `source_sklearn` OR `source_pytorch`.
* **entry_point**: The path to the Python script SageMaker runs for training and prediction.
* **source_dir**: The path to the training script directory `train_sklearn` OR `train_pytorch`.
* **entry_point**: The path to the Python script SageMaker runs for training.
* **source_dir**: The path to the training script directory `train_sklearn` OR `train_pytorch`.
* **role**: Role ARN, which was specified, above.
* **train_instance_count**: The number of training instances (should be left at 1).
* **train_instance_type**: The type of SageMaker instance for training. Note: Because Scikit-learn does not natively support GPU training, Sagemaker Scikit-learn does not currently support training on GPU instance types.
* **sagemaker_session**: The session used to train on Sagemaker.
* **hyperparameters** (optional): A dictionary `{'name':value, ..}` passed to the train function as hyperparameters.

Note: For a PyTorch model, there is another optional argument **framework_version**, which you can set to the latest version of PyTorch, `1.0`.

## EXERCISE: Define a Scikit-learn or PyTorch estimator

To import your desired estimator, use one of the following lines:
```
from sagemaker.sklearn.estimator import SKLearn
```
```
from sagemaker.pytorch import PyTorch
```
"""


# %%
# your import and estimator code, here
def build_name_from_array(model_array):
    model_name = '-'.join(model_array)
    model_name = re.sub(r"[^-a-zA-Z0-9]+", '-', model_name).strip('-')
    return re.sub(r"--+", '-', model_name)


def build_model_name(data_desc, classifier, hyperparams, count) -> str:
    hyperparams_json = json.dumps(hyperparams, sort_keys=True, ensure_ascii=True)
    model_name = build_name_from_array([
        data_desc,
        classifier,
        hyperparams_json,
        str(count),
    ])
    if len(model_name) > 63:
        hyperparams_hash = str(DeepHash(hyperparams_json)[hyperparams_json])[:8]
        model_name = build_name_from_array([
            data_desc,
            classifier,
            hyperparams_hash,
            str(count),
        ])
        if len(model_name) > 63:
            # this will error on the server, error fast
            raise ValueError(f'generated model name is too long: {model_name}')
    return model_name


def build_and_train_estimator(
    data_desc: str,
    classifier: str,
    count: int = 1,
    wait: bool = False,
    **hyperparams: object
) -> Tuple[SKLearn, str]:
    """
    Creates or returns an existing sagemaker training job

    :param data_desc: name of data to use (unique)
    :param classifier: name of sklearn classifier
    :param count: cache buster
    :param wait: waits on job, useful for debugging
    :param hyperparams: hyperparameters for the model
    :return: estimator | None
    """
    model_name = build_model_name(data_desc, classifier, hyperparams, count)
    print('model_name', model_name)

    # check if model has already been built on this data
    #  if it has check if it's finished and attach
    try:
        import boto3
        client = boto3.client('sagemaker')
        response = client.describe_training_job(
            TrainingJobName=model_name
        )
        if wait or response['TrainingJobStatus'] in ['Completed', 'Failed']:
            return SKLearn.attach(model_name), model_name
        else:
            raise Warning(f'{model_name} isn\'t finished training yet')
    except ClientError:
        pass

    output_location = f's3://{bucket}/{S3_MODEL_DIR / data_desc}'
    estimator = SKLearn(
        'train_and_deploy.py',
        source_dir='sagemaker_container',
        code_location=output_location,
        output_path=output_location,
        train_instance_type=TRAIN_INSTANCE,
        framework_version='0.23-1',
        role=role,
        hyperparameters={
            'classifier': classifier,
            **hyperparams
        })

    estimator.fit(f's3://{bucket}/{S3_FEATURE_DIR / data_desc}', wait=wait, job_name=model_name)

    return estimator, model_name


# %% [markdown]
"""
## EXERCISE: Train the estimator

Train your estimator on the training data stored in S3. This should create a training job that you can monitor in your SageMaker console.
"""

# %% jupyter={"outputs_hidden": true}
# Train your estimator on S3 training data
build_and_train_estimator('all-features', 'SVC')


# %% jupyter={"outputs_hidden": true}
# GaussianNB
for data_desc in data_to_try:
    build_and_train_estimator(data_desc, 'GaussianNB')

# %% jupyter={"outputs_hidden": true}
# SVC
for data_desc in data_to_try:
    for kernel in [
        'rbf',
        'linear',
        # 'poly',
        'sigmoid',
    ]:
        build_and_train_estimator(data_desc, 'SVC', kernel=kernel)
    build_and_train_estimator(data_desc, 'SVC', kernel='poly', count=2)

# %% jupyter={"outputs_hidden": true}
# AdaBoostClassifier
for data_desc in data_to_try:
    build_and_train_estimator(data_desc, 'AdaBoostClassifier')

# %% jupyter={"outputs_hidden": true}
# DecisionTreeClassifier
for data_desc in data_to_try:
    for criterion in ['entropy', 'gini']:
        for min_samples_split in range(2, 5):
            build_and_train_estimator(
                data_desc,
                'DecisionTreeClassifier',
                count=2,
                criterion=criterion,
                min_samples_split=min_samples_split,
            )

# %% [markdown]
"""
### Final Model
"""

# %% jupyter={"outputs_hidden": true}
estimator, model_name = build_and_train_estimator(data_desc, 'AdaBoostClassifier', count=2, wait=True)

# %% [markdown]
"""
## EXERCISE: Deploy the trained model

After training, deploy your model to create a `predictor`. If you're using a PyTorch model, you'll need to create a trained `PyTorchModel` that accepts the trained `<model>.model_data` as an input parameter and points to the provided `source_pytorch/predict.py` file as an entry point.

To deploy a trained model, you'll use `<model>.deploy`, which takes in two arguments:
* **initial_instance_count**: The number of deployed instances (1).
* **instance_type**: The type of SageMaker instance for deployment.

Note: If you run into an instance error, it may be because you chose the wrong training or deployment instance_type. It may help to refer to your previous exercise code to see which types of instances we used.
"""

# %%
# %%time
# deploy your model to create a predictor
predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type=DEPLOY_INSTANCE,
    endpoint_name=model_name + '-ep'
)

# %% [markdown]
"""
---
# Evaluating Your Model

Once your model is deployed, you can see how it performs when applied to our test data.

The provided cell below, reads in the test data, assuming it is stored locally in `data_dir` and named `test.csv`. The labels and features are extracted from the `.csv` file.
"""

# %%
"""
DON'T MODIFY ANYTHING IN THIS CELL THAT IS BELOW THIS LINE
"""

# read in test data, assuming it is stored locally
test_data = pd.read_csv(os.path.join(OUTPUT_DIR / data_to_try[0], "test.csv"), header=None, names=None)

# labels are in the first column
test_labels = test_data.iloc[:, 0]
test_features = test_data.iloc[:, 1:]

# %% [markdown]
"""
## EXERCISE: Determine the accuracy of your model

Use your deployed `predictor` to generate predicted, class labels for the test data. Compare those to the *true* labels, `test_y`, and calculate the accuracy as a value between 0 and 1.0 that indicates the fraction of test data that your model classified correctly. You may use [sklearn.metrics](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics) for this calculation.

**To pass this project, your model should get at least 90% test accuracy.**
"""

# %%
# First: generate predicted, class labels
# noinspection PyTypeChecker
predict_labels: np.ndarray = predictor.predict(test_features)  # `.predict` doesn't have a return type defined

"""
DON'T MODIFY ANYTHING IN THIS CELL THAT IS BELOW THIS LINE
"""
# test that your model generates the correct number of labels
assert len(predict_labels) == len(test_labels), 'Unexpected number of predictions.'
print('Test passed!')

# %%
# Second: calculate the test accuracy
accuracy = accuracy_score(predict_labels, test_labels)

print(accuracy)

# %% [markdown]
"""
### Question 1: How many false positives and false negatives did your model produce, if any? And why do you think this is?
"""

# %% [markdown]
"""
**Answer**:

The count of false positives and false negatives are in the next cell.

> And why do you think this is?

This models accuracy is not 100%.
This means that it has to have at least some incorrect (aka false) results.

False negatives are when a positive value is predicted to be a negative value. This is a
"""

# %%
test_labels = test_labels.to_numpy().astype(bool)
predict_labels = predict_labels.astype(bool)

# %%
true_positives = (predict_labels & test_labels).sum()
false_positives = (predict_labels & ~test_labels).sum()
true_negatives = (~predict_labels & ~test_labels).sum()
false_negatives = (~predict_labels & test_labels).sum()
len(test_labels), true_positives, false_positives, true_negatives, false_negatives

# %%
assert (true_positives + false_positives + true_negatives + false_negatives) == len(test_labels), \
    'All cases should sum to the number of instances'
assert true_positives + false_positives == predict_labels.sum(), \
    'number of positives (true + false) should equal the number of positives in the predict set'
assert true_negatives + false_negatives == (len(predict_labels) - predict_labels.sum()), \
    'number of negatives (true + false) should equal the number of negatives in the predict set'
assert true_positives + false_negatives == test_labels.sum(), \
    'true pos + false neg should equal the number of positives in the test set'
assert true_negatives + false_positives == (len(test_labels) - test_labels.sum()), \
    'true neg + false pos should equal the number of negatives in the test set'

print('number of false positives', false_positives)
print('number of false negatives', false_negatives)

# %% [markdown]
"""
### Question 2: How did you decide on the type of model to use?
"""

# %% [markdown]
"""
**Answer**:

We were looking for a 90%+ accuracy score.
A number of scikit-learn models can achieve this level of accuracy on a dataset this size with fairly low computation requirements.
Given the type of data, Naïve Bayes, SVM, or a Decision Tree model seemed likely to work.
Given all this information, a search of the given models with stopping at 90% accuracy seemed like the fastest way to finish the requirements.

Search criteria:
- features
    - start with all features
    - remove low correlated features in a second and third round
- models & parameters:
    - Naïve Bayes
        - GaussianNB
    - SVM
        - kernel: 'rbf', 'linear', 'poly', or 'sigmoid'
    - Ada Boost
        - Default
    - Random Forest
        - criterion: 'entropy', 'gini'
        - min_samples_split: 2, 3, 4, 5
- stopping conditions:
    - more than 90% accuracy
    - more than 3 hours spent in training
- continue iterating on model, parameters, and features until a stopping condition is met

These search parameters found a model that achieved over 90% accuracy in the first hour of training, so much of the search was not completed.
In a work environment if we were looking for an accuracy of 90% and achieved it we would stop our search and start the deployment process in order to gain as much benefit from the improvement as possible.
After a round of deployment and verifying the results we would most-likely circle back on improving this model further since it's most likely possible to get a higher accuracy with it's most likely possible to get a higher accuracy with a little more work.

If this search hadn't found the results we were looking for it would have given us a lot of information to point us in a new direction for where to go next

#### Ways to improve:

Use a hyperparameter tuning job:

Ideally the hyperparameter tuning solution from sagemaker would have been used.
This would have required implementing a container that could be used with the hyperparameter tuning job and defining a tuning job per model.
A hyperparameter tuning job would have searched the solution space more effectively and could have been used to avoid the training instance limit.
This would have been more efficient than looping over the solution space.
"""

# %% [markdown]
"""
----
## EXERCISE: Clean up Resources

After you're done evaluating your model, **delete your model endpoint**. You can do this with a call to `.delete_endpoint()`. You need to show, in this notebook, that the endpoint was deleted. Any other resources, you may delete from the AWS console, and you will find more instructions on cleaning up all your resources, below.
"""

# %%
# uncomment and fill in the line below!
predictor.delete_endpoint()

