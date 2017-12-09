# Goncalo Marques - 84719 e Manuel Sousa - 84740 (Grupo 22)
import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.svm import SVR
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
    #Accuracy: -0.17; -582.91
    #reg = SVR(C=1000, gamma=0.1)

    #Accuracy: -0.10; -547.94
    reg = KernelRidge(alpha=0.001, kernel='rbf', gamma=0.1)
    reg.fit(X,Y)

    #cv = cross_val_score(reg, X, Y, scoring='neg_mean_squared_error', cv=5)
    #print("cv: ", cv)
    #print("Accuracy: %0.2f (+/- %0.2f)" % (cv.mean(), cv.std() * 2))

    return reg

def myprediction(X,reg):
    Ypred = reg.predict(X)
    return Ypred
