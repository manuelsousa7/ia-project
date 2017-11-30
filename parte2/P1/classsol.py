import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

vowels = ['a','e','i','o','u','á','à','â','ã','é','è','ê','í','ì','î','ó','ò','õ','ô','ú','ù','û']

def features(X):
    
    # len, numberOfVowels, numberOfConsonants, percentageOfVowels, percentageOfConsonants, evenWord
    # evenVowels, 
    
    functions = [numberOfVowels, evenVowels, wordHasR]
    #BEST: len, numberOfVowels, evenWord
    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        for i in range(len(functions)):
            F[x, i] = functions[i](X[x])

    return F

def numberOfVowels(X):
    count = 0
    for letter in X:
        if (letter in vowels):
            count+=1
    return count

def wordHasR(X):
    return not 'r' in X

def numberOfConsonants(X):
    vowels = ['a','e','i','o','u','á','à','â','ã','é','è','ê','í','ì','î','ó','ò','õ','ô','ú','ù','û']
    count = 0
    for letter in X:
        if (not (letter in vowels)):
            count+=1
    return count

def percentageOfVowels(X):
    count = 0
    vowelCount = 0
    for letter in X:
        count+=1
        if (letter in vowels):
            vowelCount+=1

    return vowelCount/count

def percentageOfConsonants(X):
    return 1 - percentageOfVowels(X)

def evenWord(X):
    return len(X) % 2 == 0

def evenVowels(X):
    return numberOfVowels(X) % 2 == 0

def repeatsWords(X):
    for i in range(len(X)):
        if (X[i] in X[:i] or X[i] in X[i+1:]):
            return True
    return False
    

def mytraining(f,Y):
    #Ambos funcionam
    #clf = neighbors.KNeighborsClassifier(5, weights='uniform')
    clf = linear_model.SGDClassifier()
    clf = clf.fit(f, Y)
   
    return clf
    
def mytrainingaux(f,Y,par):
    
    return 0

def myprediction(f, clf):
    Ypred = clf.predict(f)

    return Ypred