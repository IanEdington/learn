import pickle
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_extraction.text import TfidfVectorizer

CACHE_DIR = Path("data", "cache", "preprocess_emails")

local_cache = {}

def build_data(percentile_of_features):
    with open("data/email_authors.pkl", 'rb') as authors_file, open("data/word_data.pkl", 'rb') as word_file:
        email_authors = pickle.load(authors_file)
        word_data = pickle.load(word_file)

    # split into training and test
    features_train, features_test, labels_train, labels_test = train_test_split(word_data, email_authors, test_size=0.1, random_state=42)

    # tokenize emails
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed = vectorizer.transform(features_test)

    # only use top 10% of features
    selector = SelectPercentile(percentile=percentile_of_features)
    features_train_transformed = selector.fit_transform(features_train_transformed, labels_train).toarray()
    features_test_transformed = selector.transform(features_test_transformed).toarray()

    return [features_train_transformed, features_test_transformed, labels_train, labels_test]

def preprocess_emails(percentile_of_features = 10):
    file_name = f'preprocess_emails_{str(percentile_of_features)}.pkl'

    # early return if values are cached in memory
    if local_cache.get(file_name) is not None:
        return local_cache.get(file_name)

    cache_file = CACHE_DIR / file_name

    # early return if values are cache
    if cache_file.exists():
        with open(cache_file, 'rb') as f:
            loaded = pickle.load(f)
            local_cache[file_name] = loaded
            return loaded

    data = build_data(percentile_of_features)

    # cache values
    local_cache[file_name]= data
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    with open(cache_file, 'wb') as f:
        pickle.dump(data, f)
    
    return data
