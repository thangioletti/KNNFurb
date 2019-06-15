import scipy.io as scipy
import math
import numpy as np
import operator
import pandas as pd

def dist(v1, v2):
    dim, soma = len(v1), 0
    for i in range(dim):
	    soma += math.pow(v1[i] - v2[i], 2)
    return math.sqrt(soma)

def meuKnn(dadosTrain, rotuloTrain, dadosTeste, rotuloTeste, k):
    distancia = []
    #Calcula a distancia para todods os pontos de teste e treinamento
    for i in range(len(dadosTeste)):
        distanciaLinha = []
        for j in range(len(dadosTrain)):
            distanciaLinha.append([j, dist(dadosTeste[i], dadosTrain[j])])
        distanciaLinha = sorted(distanciaLinha, key=operator.itemgetter(1))
        distancia.append(distanciaLinha)

     #Calcula a acuracia
    acuracia = 0
    for i in range(len(dadosTeste)):
        rotulos = []
        for j in range(k):
            rotulos.append(rotuloTrain[distancia[i][j][0]][0])
        rotulos = pd.Series(rotulos)

        if rotulos.mode()[0] == rotuloTeste[i][0]:
            acuracia = acuracia + 1

    acuracia = acuracia/len(dadosTrain)*100
    return acuracia

def normalizacao(dados):

    for j in range(len(dados[0])):
        maior = 0
        #pega o maior dessa coluna
        for i in range(len(dados)):
            if dados[i][j] > maior:
                maior = dados[i][j]

        #normaliza entre valores de 0...1
        for i in range(len(dados)):
            dados[i][j] = dados[i][j]/maior

    return dados


mat = scipy.loadmat('grupoDados2.mat')
grupoTest  = mat['grupoTest']
grupoTrain = mat['grupoTrain']
trainRots  = mat['trainRots']
testRots   = mat['testRots']

grupoTest = normalizacao(grupoTest)
grupoTrain = normalizacao(grupoTrain)

print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 1))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 2))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 3))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 4))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 5))

#Q1.1 = k = 3, 4, 6 possuem acuracia = 98
#Q1.2 =
#Q2.1 = 72
#Q2.2 =
#Q3.1 =
#Q3.2 =
