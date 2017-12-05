import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
    #Tem de funcionar os dois
    reg = tree.DecisionTreeRegressor(criterion=’mse’, splitter=’best’, max_depth=None, \
                                    min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, \
                                    max_features=None, random_state=None, max_leaf_nodes=None, \
                                    min_impurity_decrease=0.0, min_impurity_split=None, presort=False)
    reg = KernelRidge(alpha=1, kernel=’linear’, gamma=None, degree=3, coef0=1, kernel_params=None)
    reg.fit(X,Y)
    return reg
    
def mytrainingaux(X,Y,par):
    
    #reg.fit(X,Y)
    return

def myprediction(X,reg):

    Ypred = reg.predict(X)

    return Ypred
