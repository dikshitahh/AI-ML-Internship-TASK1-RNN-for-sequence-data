from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

max_features = 10000
maxlen = 200

def load_preprocessed_data():
    (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=max_features)

    X_train = pad_sequences(X_train, maxlen=maxlen)
    X_test = pad_sequences(X_test, maxlen=maxlen)

    return X_train, y_train, X_test, y_test
