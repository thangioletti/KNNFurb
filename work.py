import scipy.io as scipy
import math
import numpy as np
import operator
import pandas as pd

lines = 50
columns = 100
k = 7

mat = scipy.loadmat('grupoDados1.mat')
grupoTest  = mat['grupoTest']
grupoTrain = mat['grupoTrain']
trainRots  = mat['trainRots']
testRots   = mat['testRots']

print(len(grupoTest))
print(len(grupoTrain))
def dist(v1, v2):
    dim, soma = len(v1), 0
    for i in range(dim):
	    soma += math.pow(v1[i] - v2[i], 2)
    return math.sqrt(soma)

distancia = []
for i in range(lines):
    distanciaLinha = []
    for j in range(columns):
        distanciaLinha.append([j, dist(grupoTest[i], grupoTrain[j])])
    distanciaLinha = sorted(distanciaLinha, key=operator.itemgetter(1))
    distancia.append(distanciaLinha)

acuracia = 0
for i in range(lines):
    rotulos = []
    for j in range(k):
        rotulos.append(trainRots[distancia[i][j][0]][0])
    rotulos = pd.Series(rotulos)

    if rotulos.mode()[0] == testRots[i][0]:
        acuracia = acuracia + 1

acuracia = acuracia/lines*100
print(acuracia)

#Q1.1 = k = 3, 4, 6