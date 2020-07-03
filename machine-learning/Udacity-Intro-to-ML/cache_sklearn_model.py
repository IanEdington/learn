import pickle
from pathlib import Path
from time import time

from deepdiff import DeepHash

PROJECT_DIR = Path(__file__).parent
DATA_DIR = PROJECT_DIR / 'data'
CACHE_FOLDER = DATA_DIR / 'cache'


def get_hash_of_model_and_data(model, data_description):
    hashable_description = [data_description, type(model).__name__, model.get_params()]
    return DeepHash(hashable_description)[hashable_description]


def get_model_cache_file(model, data_description):
    model_hash = get_hash_of_model_and_data(model, data_description)
    return CACHE_FOLDER / data_description / type(model).__name__ / f'{model_hash}.pkl'


def retrieve_cached_model(model, data_description):
    file_name = get_model_cache_file(model, data_description)

    if file_name.exists():
        with open(file_name, 'rb') as f:
            retrieved = pickle.load(f)
            retrieved_model = retrieved.get("model")

            if (
                model.get_params() == retrieved_model.get_params() and
                data_description == retrieved.get("data_description")
            ):
                return [True, retrieved_model, retrieved.get("meta")]
            else:
                print("model.get_params()", model.get_params())
                print("retrieved_model.get_params()", retrieved_model.get_params())
                print("data_description", data_description)
                print("retrieved.get(\"data_description\")", retrieved.get("data_description"))
                print("retrieved.get(\"data_desciption\")", retrieved.get("data_desciption"))
                raise Exception('params are not equal, might be caused by a hash collision')

    return [False, model, {}]


def save_cached_model(model, data_description, meta):
    file_name = get_model_cache_file(model, data_description)

    file_name.parent.mkdir(parents=True, exist_ok=True)

    with open(file_name, 'wb') as f:
        pickle.dump({"model": model, "data_description": data_description, "meta": meta}, f)


def train_model_cached(data_desc, clf, features_train, labels_train):
    [is_restored, clf, meta] = retrieve_cached_model(clf, data_desc)

    fit_delta = meta.get("fit_time_sec")
    if not is_restored:
        t = time()
        clf.fit(features_train, labels_train)
        fit_delta = round(time() - t, 3)
        save_cached_model(clf, data_desc, {
            "fit_time_sec": fit_delta,
        })

    return clf, fit_delta
