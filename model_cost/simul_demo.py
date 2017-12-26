# This python file simulates and computes the model costs as in SI S4.2

import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import metrics
from sklearn.metrics import *

nsense = np.asarray([5,10,15,20,25,30])
ninitial = 10
nrun = 20

models = ['exemplar','progenitor','prototype','local','chain']
modelabbrev = ['ex.','prog.','prot.','loc.','nn']

# Generate a 2D space (random sampling positions)
def genRand2DSpace(n):
# n: number of senses

    X = np.zeros([n,2])
    for i in range(0,2):
        X[:,i] = np.random.uniform(0,1,n)

    return X
    
# Define models
def computeModelCost(Coords,m,k,n):
# Coords: coordinates of all points/senses in 2D
# m: model name
# k: index of initial seed pointed within Coords
# n: number of senses

    pairD = sklearn.metrics.pairwise.euclidean_distances(Coords,Coords)
    existS = np.asarray(k)
    newS = np.delete(np.arange(n),k)
    indLocal = existS
    indProto = existS
    c = 0
    cnt = 0

    while len(newS) > 0:

        
        if m == 'exemplar':
    
            if cnt == n-1:
                pairDexemp = pairD[np.ix_([newS],existS)]
            elif cnt == 0:
                pairDexemp = pairD[np.ix_(newS,[existS])]
            else:
                pairDexemp = pairD[np.ix_(newS,existS)]
                
        # dvec to average existing senses
            dvec = []
            for cc in range(0,len(newS)):
                dvec.append(np.mean(pairDexemp[cc,:]))
            dvec = np.asarray(dvec)
            
        elif m == 'progenitor':
        
        # dvec to just initial sense
            dvec = pairD[newS,k]
            
        elif m == 'prototype':
        
        # dvec to moving prototype
            dvec = pairD[newS,indProto]
            
        elif m == 'local':
        
        # dvec to last emerging sense
            dvec = pairD[newS,indLocal]
          
        elif m == 'chain':
            
            if cnt == n-1:
                pairDchain = pairD[np.ix_([newS],existS)]
            elif cnt == 0:
                pairDchain = pairD[np.ix_(newS,[existS])]
            else:
                pairDchain = pairD[np.ix_(newS,existS)]
            
        # dvec to minimal neighbor sense
            dvec = []
            for cc in range(0,len(newS)):
                dvec.append(np.min(pairDchain[cc,:]))
            dvec = np.asarray(dvec)
        
        if len(newS) > 1:
            # Prepare prob vector according to Luce
            pvec = np.exp(-dvec)
            pvec = pvec / np.sum(pvec)
            samp = np.random.multinomial(1,pvec)
            indPop = np.where(samp==1)[0][0]
            # Update cost
            c = c + dvec[indPop]
            # Update relevant indices for local model
            indLocal = newS[indPop]
            # Pop the predicted sense
            existS = np.append(existS,newS[indPop])
            newS = np.delete(newS,indPop)
            # Update relevant indices for prototype model (moving)
            pairDproto = np.sum(pairD[np.ix_(existS,existS)],axis=1)
            indProto = np.where(pairDproto==min(pairDproto))[0][0]
            indProto = existS[indProto]
        else:
            c = c + dvec
            newS = []
        
        cnt = cnt + 1
        
    return c


# Run simulation
cnt = 1

fig = plt.figure(figsize=(10,8))

for s in nsense:
    
    print('#senses = '+str(s))
    
    # Different configurations of space
    for i in range(0,ninitial):
        
        MinTally = np.zeros([s,len(models)])
        
        Coords = genRand2DSpace(s)
        
        # Iterate over each possible initial sense
        for k in range(0,s):
            
            # Multiple runs for a given space + initial seed
            for j in range(0,nrun):
                                
                cost = np.zeros(len(models))
                mi = 0
                
                for m in models:
                        
                    cost[mi] = computeModelCost(Coords,m,k,s)
                    mi = mi + 1
                    
                minimalind = np.where(cost==np.min(cost))[0][0]  
                MinTally[k,minimalind] = MinTally[k,minimalind] + 1
    
    plt.subplot(2,3,cnt)
    plt.bar(np.arange(len(models)),np.sum(MinTally,axis=0))
    plt.xticks(np.arange(len(models)),modelabbrev)
    plt.title('n = '+str(s))
    if (cnt == 1) or (cnt == 4):
        plt.ylabel('Min. cost count')
            
    cnt = cnt + 1

#plt.savefig('simul_model.eps',dpi=600)

plt.show()