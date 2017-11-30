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
        #F[x,3] = percentageOfConsonants(X[x]) --> NAO FUNCIONA

    return F

def numberOfVowels(X):
    vowels = ['a','e','i','o','u','á','à','â','ã','é','è','ê','í','ì','î','ó','ò','õ','ô','ú','ù','û']
    count = 0
    for letter in X:
        if (letter in vowels):
            count+=1
    return count

def percentageOfVowels(X):
    count = 0
    vowelCount = 0
    vowels = ['a','e','i','o','u','á','à','â','ã','é','è','ê','í','ì','î','ó','ò','õ','ô','ú','ù','û']
    for letter in X:
        count+=1
        if (letter in vowels):
            vowelCount+=1

    return vowelCount/count

def percentageOfConsonants(X):
    return 1 - percentageOfVowels(X)

def numberOfConsonants(X):
    vowels = ['a','e','i','o','u','á','à','â','ã','é','è','ê','í','ì','î','ó','ò','õ','ô','ú','ù','û']
    count = 0
    for letter in X:
        if (not (letter in vowels)):
            count+=1
    return count

def mytraining(f,Y):
    #Ambos funcionam
    clf = neighbors.KNeighborsClassifier(2, weights='uniform')
    #clf = linear_model.SGDClassifier()
    clf = clf.fit(f, Y)
   
    return clf
    
def mytrainingaux(f,Y,par):
    
    return 0

def myprediction(f, clf):
    Ypred = clf.predict(f)

    return Ypred