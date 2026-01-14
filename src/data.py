from sklearn.datasets import fetch_openml
import numpy as np


def load_mnist():

    mnist = fetch_openml('mnist_784', as_frame=False)
    X, y = mnist.data, mnist.target

    return X, y

X, y = load_mnist()
print(y.shape)



def split_train_test(X, y):
    X_train, X_test = X[:60000], X[60000:]
    y_train, y_test = y[:60000], y[60000:]
    return X_train, X_test, y_train, y_test
