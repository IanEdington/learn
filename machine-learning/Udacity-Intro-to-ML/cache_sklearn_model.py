import pickle
from pathlib import Path
from deepdiff import DeepHash

CACHE_FOLDER = Path("data", "cache")

def retrieve_cached_model(model, data_desciption):
    hashable_description = [data_desciption, model.get_params()]
    model_hash = DeepHash(hashable_description)[hashable_description]
    file_name = CACHE_FOLDER / type(model).__name__ / f'{model_hash}.pkl'

    if (file_name.exists()):
        with open(file_name, 'rb') as f:
            retrieved = pickle.load(f)
            retrieved_model = retrieved.get("model")
            if (model.get_params() == retrieved_model.get_params()):
                return [True, retrieved_model, retrieved.get("meta")]
            else:
                raise Exception('params are not equal, might be caused by a hash collision')
    return [False, model, {}]

def save_cached_model(model, data_desciption, meta):
    hashable_description = [data_desciption, model.get_params()]
    model_hash = DeepHash(hashable_description)[hashable_description]
    file_name = CACHE_FOLDER / type(model).__name__ / f'{model_hash}.pkl'

    file_name.parent.mkdir(parents=True, exist_ok=True)

    with open(file_name, 'wb') as f:
        pickle.dump({"model": model, "meta": meta}, f)
