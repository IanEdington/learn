import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_emails():
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
    selector = SelectPercentile(percentile=10)
    features_train_transformed = selector.fit_transform(features_train_transformed, labels_train).toarray()
    features_test_transformed = selector.transform(features_test_transformed).toarray()

    return features_train_transformed, features_test_transformed, labels_train, labels_test