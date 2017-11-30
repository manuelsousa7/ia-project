import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
    #reg = linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=1)
    reg = linear_model.Ridge(alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, max_iter=None, tol=0.001, solver='auto', random_state=None)
    reg.fit(X,Y)
    return reg
    
def mytrainingaux(X,Y,par):
    
    #reg.fit(X,Y)
    return reg

def myprediction(X,reg):

    Ypred = reg.predict(X)

    return Ypred
