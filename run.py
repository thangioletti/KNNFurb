# Autores: Alex Seródio, Luma Kuhl, Matheus Losi e Tiago Henrique Angioletti

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

def meuKnn(grupoTrain, trainRots, grupoTest, rotuloTeste, k):

    distancia = []
    #Calcula a distancia para todods os pontos de teste e treinamento
    for i in range(len(grupoTest)):
        distanciaLinha = []
        for j in range(len(grupoTrain)):
            distanciaLinha.append([j, dist(grupoTest[i], grupoTrain[j])])
        distanciaLinha = sorted(distanciaLinha, key=operator.itemgetter(1))
        distancia.append(distanciaLinha)

    #Calcula a acuracia
    acuracia = 0
    for i in range(len(grupoTest)):
        rotulos = []
        for j in range(k):
            rotulos.append(trainRots[distancia[i][j][0]][0])
        rotulos = pd.Series(rotulos)

        if rotulos.mode()[0] == testRots[i][0]:
            acuracia = acuracia + 1

    acuracia = acuracia/len(grupoTest)*100
    return acuracia

def normalizacao(dadosTrain, dadosTeste):

    for j in range(len(dadosTrain[0])):
        maior = 0
        menor = 0
        #pega o maior dessa coluna
        for i in range(len(dadosTrain)):
            if dadosTrain[i][j] > maior:
                maior = dadosTrain[i][j]
            if dadosTrain[i][j] < menor:
                menor = dadosTrain[i][j]

        #normaliza entre valores de 0...1 o treinamento
        for i in range(len(dadosTrain)):
            dadosTrain[i][j] = round((dadosTrain[i][j]-menor)/(maior-menor),2)
        for i in range(len(dadosTeste)):
            dadosTeste[i][j] = round((dadosTeste[i][j]-menor)/(maior-menor),2)


mat = scipy.loadmat('grupoDados3.mat')
grupoTest  = mat['grupoTest']
grupoTrain = mat['grupoTrain']
trainRots  = mat['trainRots']
testRots   = mat['testRots']

normalizacao(grupoTrain, grupoTest)

print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 1))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 2))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 3))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 4))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 5))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 6))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 7))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 8))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 9))
print(meuKnn(grupoTrain, trainRots, grupoTest, testRots, 10))

#Q1.1 = k = 2 acuracia = 96
#Q1.2 = Não. Descartando o último atributo ainda conseguimos manter uma acurácia de 96%. Porém ao descartar duas características a acurácia cai para 72%
#Q2.1 = Sem normalização acuracia = 68
#Q2.2 = Com normalização dos dados e k = 1 já chegou a 98
#Q3.1 = k = 1 sem normalização acuracia chegou a 70, com normalização chegou a 68
#Q3.2 = k = 9 chegou a 94% de acuracia com os dados normalizados
