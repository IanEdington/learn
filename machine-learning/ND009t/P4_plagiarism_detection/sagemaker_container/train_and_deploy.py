from __future__ import print_function

import json
import os
from time import time

import joblib
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

RANDOM_SEED = 28
CLASSIFIERS = {
    'SVC': SVC,
    'GaussianNB': GaussianNB,
    'DecisionTreeClassifier': DecisionTreeClassifier,
    'AdaBoostClassifier': AdaBoostClassifier,
}


# Provided model load function
def model_fn(model_dir):
    """Load model from the model_dir. This is the same model that is saved
    in the main if statement.
    """
    print("Loading model.")

    # load using joblib
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    print("Done loading model.")

    return model


def get_data_by_desc(data_desc):
    test_data = pd.read_csv(os.path.join(data_desc, 'test.csv'), header=None, names=None)
    test_features = test_data.iloc[:, 1:]
    test_labels = test_data.iloc[:, 0]

    train_data = pd.read_csv(os.path.join(data_desc, 'train.csv'), header=None, names=None)
    train_features = train_data.iloc[:, 1:]
    train_labels = train_data.iloc[:, 0]

    return train_features, train_labels, test_features, test_labels


if __name__ == '__main__':
    # All of the model parameters and training parameters are sent as arguments
    # when this script is executed, during a training job

    # Here we set up an argument parser to easily access the parameters

    print('environment: ', os.environ)

    # SageMaker parameters, like the directories for training data and saving models; set automatically
    # Do not need to change
    output_dir = os.environ['SM_OUTPUT_DATA_DIR']
    model_dir = os.environ['SM_MODEL_DIR']
    data_dir = os.environ['SM_CHANNEL_TRAINING']

    # --- Your code here --- ##
    # hyperparameters sent by the client are passed as command-line arguments to the script.
    with open(os.environ['SM_INPUT_TRAINING_CONFIG_FILE'], 'r') as f:
        print('loading hyperparameters')
        hyperparameters = json.load(f)
        print('hyperparameters initial:', json.dumps(hyperparameters))
        for param in list(hyperparameters):
            # delete all sagemaker hyperparameters
            value = hyperparameters.get(param)
            if param.startswith('sagemaker_'):
                del hyperparameters[param]
            # remove extra `"` added to params
            elif isinstance(value, str):
                hyperparameters[param] = value.strip('"')
                # make true and false True and False
                if value.lower() == 'true':
                    hyperparameters[param] = True
                elif value.lower() == 'false':
                    hyperparameters[param] = False
                # convert integers
                elif value.isdigit():
                    hyperparameters[param] = int(value)
                # convert float
                elif value.replace('.', '', 1).isdigit():
                    hyperparameters[param] = float(value)

        print('hyperparameters:', json.dumps(hyperparameters))

    # Read in csv training file
    train_features, train_labels, test_features, test_labels = get_data_by_desc(data_dir)

    # Define the model
    classifier = hyperparameters['classifier']
    del hyperparameters['classifier']
    classifier_class = CLASSIFIERS.get(classifier)
    if not classifier_class:
        raise ValueError(f'classifier {classifier} not found in CLASSIFIERS, import and add it')

    print('hyperparameters passed to model: ', json.dumps(hyperparameters))
    model = classifier_class(**hyperparameters)

    # for models that can use multiple CPUs use them all
    if hasattr(model, 'n_jobs'):
        model.n_jobs = -1
    if hasattr(model, 'random_state'):
        model.random_state = RANDOM_SEED

    # Train the model
    model.fit(train_features, train_labels)

    # Evaluate the model
    # - inference speed
    t = time()
    predict_labels = model.predict(test_features)
    inference_speed_per_record = (time() - t) / len(predict_labels)

    # - accuracy score
    # - recall
    # - precision
    report = classification_report(test_labels, predict_labels, output_dict=True)
    print('classification_report: ', classifier_class)
    # to measure metrics just print the variables separated by `;`
    print(f"accuracy: {report['accuracy']}; "
          f"recall: {report['1.0']['recall']}; "
          f"precision: {report['1.0']['precision']}; "
          f"f1_score: {report['1.0']['f1-score']}; "
          f"inference_speed: {inference_speed_per_record}")

    classifier_performance = {
        "classifier": type(model).__name__,
        "data_description": data_dir,
        "params": model.get_params(),
        "accuracy": report['accuracy'],
        "recall": report['1.0']['recall'],
        "precision": report['1.0']['precision'],
        "f1_score": report['1.0']['f1-score'],
        "inference_speed": inference_speed_per_record,
    }
    # save test metrics with model
    with open(os.path.join(output_dir, 'performance.json'), 'w') as f:
        json.dump(classifier_performance, f)

    # --- End of your code  --- ##

    # Save the trained model
    joblib.dump(model, os.path.join(model_dir, "model.joblib"))
