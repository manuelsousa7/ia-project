# Goncalo Marques - 84719 e Manuel Sousa - 84740 (Grupo 1)
import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

import hashlib

from random import shuffle

vowels = ['a','e','i','o','u','á','à','â','ã','é','è','ê','í','ì','î','ó','ò','õ','ô','ú','ù','û']
acentos = ['á','à','â','ã','é','è','ê','í','ì','î','ó','ò','õ','ô','ú','ù','û']


def features(X):
    
    # len, numberOfVowels, numberOfConsonants, percentageOfVowels, percentageOfConsonants, evenWord, sameLetters
    # evenVowels, 
    
    functions = [repeatsWords] #Alterar lista para nome de funcoes aka features (O processo é automatico)
    #BEST: len, numberOfVowels, evenWord
    #BEST 50 k neigh: len, numberOfVowels, numberOfConsonants
    F = np.zeros((len(X),len(functions)))
    for x in range(0,len(X)):
        for i in range(len(functions)):
            F[x, i] = functions[i](X[x])
    return F

def uniqueNumber (X):
    return int.from_bytes(X.encode(), 'little')

def numberOfVowels(X):
    count = 0
    for letter in X:
        if (letter in vowels):
            count+=1
    return count

def wordHasR(X):
    return not 'r' in X

def totalASCII(X):
    soma = 0
    for i in X:
        soma += ord(i)
    return soma

def countAcentos(X):
    count = 0
    for i in X:
        if(i in acentos):
            count += 1
    return count
        
def numberOfConsonants(X):
    count = 0
    for letter in X:
        if (not (letter in vowels)):
            count+=1
    return count

def sameLetters(X):
    trueList = ["útil"]
    falseList = ["rir","seara"]
    dic = {}
    countT = countF = 0
    for i in trueList:
        for l in i:
            dic[l] = True
    for i in falseList:
        for l in i:
            dic[l] = False
    for l in X:
        if(l not in dic or dic[l] == False):
            countF += 1
        else:
            countT += 1
    return countT > countF
            

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
    clf = neighbors.KNeighborsClassifier(1)
    #clf = linear_model.LinearRegression()
    clf = clf.fit(f, Y)
   
    return clf
    
def mytrainingaux(f,Y,par):
    
    return 0

def myprediction(f, clf):
    Ypred = clf.predict(f)

    return Ypred