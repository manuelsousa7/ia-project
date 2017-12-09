# Goncalo Marques - 84719 e Manuel Sousa - 84740 (Grupo 22)
# -*- coding: utf-8 -*-
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
        newQ = np.zeros((self.nS,self.nA))
        
        while True:            
            for tt in trace:
                #[x, a, y, r]
                newQ[int(tt[0]),int(tt[1])] = newQ[int(tt[0]),int(tt[1])] + self.alpha * (tt[3] + self.gamma * max(newQ[int(tt[2]),:]) - newQ[int(tt[0]),int(tt[1])])
            err = np.linalg.norm(self.Q-newQ)
            self.Q = np.copy(newQ)
            if err < self.threshold:
                break 
        
        return self.Q




            