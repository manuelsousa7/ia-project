# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:31:54 2017

@author: mlopes
"""
import numpy as np

def Q2pol(Q, eta=5):

    politica = np.zeros(Q.shape)
    for i in range(Q.shape[0]):
        for j in range(Q.shape[1]):
            politica[i][j] = int(Q[i][j] == max(Q[i]))
    return politica
	
class myRL:

    def __init__(self, nS, nA, gamma):
        self.nS = nS
        self.nA = nA
        self.gamma = gamma
        self.alpha = 0.14
        self.threshold = 1e-2
        self.Q = np.zeros((nS,nA))
        
    def traces2Q(self, trace):
        nQ = np.zeros((self.nS,self.nA))
        ii = 0
        while True:            
            for tt in trace:
                #[x, a, y, r]
                nQ[int(tt[0]),int(tt[1])] = nQ[int(tt[0]),int(tt[1])] + self.alpha * (tt[3] + self.gamma * max(nQ[int(tt[2]),:]) - nQ[int(tt[0]),int(tt[1])])
            err = np.linalg.norm(self.Q-nQ)
            self.Q = np.copy(nQ)
            if err < self.threshold:
                break 
            ii += 1
        
        return self.Q




            