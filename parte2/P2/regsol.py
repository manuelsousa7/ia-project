import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.svm import SVR
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
    #Accuracy: -0.17; -62.50
    #reg = SVR(C=1000, gamma=0.1)

    #Accuracy: -0.12; -37.23
    reg = KernelRidge(alpha=0.001, kernel='rbf', gamma=0.1)
    reg.fit(X,Y)

    """
    cv = cross_val_score(reg, X, Y, scoring='neg_mean_squared_error', cv=13)
    print("cv: ", cv)
    print("Accuracy: %0.2f (+/- %0.2f)" % (cv.mean(), cv.std() * 2))
    """

    return reg

def myprediction(X,reg):
    Ypred = reg.predict(X)
    return Ypred
