import numpy as np
from sklearn import datasets, tree, linear_model, svm
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
    reg = svm.NuSVC(C=1000, gamma=0.1)
    #labels= labels.reshape((N,))
    #labels.ravel()
    #Funciona nos dois exemplos
    #reg = KernelRidge(alpha=0.001, kernel='rbf', gamma=0.1)
    reg.fit(X,Y)
    return reg

def myprediction(X,reg):
    Ypred = reg.predict(X)
    return Ypred
