import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

def features(X):
    
    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        F[x,0] = len(X[x])
        F[x,1] = numberOfVowels(X[x])
        F[x,2] = numberOfConsonants(X[x])
        F[x,3] = #Percentagem de vogais
        F[x,4] = #Numero/Percentagem de caracteres esquisitos? (ç Ù)...

    return F

def numberOfVowels(X):
    count = 0
    if (letter in X == "a" or "e" or "i" or "o" or "u"):
        count++
    return count

def numberOfConsonants(X):
    count = 0
    if (not (letter in X == "a" or "e" or "i" or "o" or "u")):
        count++
    return count

def mytraining(f,Y):
    clf = #Implementar
    clf = clf.fit(f, Y)
   
    return clf
    
def mytrainingaux(f,Y,par):
    
    return clf

def myprediction(f, clf):
    Ypred = clf.predict(f)

    return Ypred

print(numberOfVowels("Lolitos"))