#!/usr/bin/python3
"""Main"""
import numpy as np
from mllib.supervised import LinearRegression, LogisticRegressionClassifier

if __name__ != '__main__':
    clf = LinearRegression()
    X_train = np.array([[1, 2, 5], [2, 3, 4], [3, 4, 3]])
    print(X_train.dtype)
    y_train = np.array([[1], [2], [3]])
    X_test = np.array([[4, 2, 2], [5, 2, 1]])
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    print(pred)

else:
    clf = LogisticRegressionClassifier()
    X_train = np.array([[2], [3], [7], [6], [1], [8]])
    y_train = np.array([[-1], [-1], [1], [1], [-1], [1]])
    clf.fit(X_train, y_train)
    pred = clf.predict(np.array([[2.5], [5.5], [8], [4.5]]))
    print(pred)
