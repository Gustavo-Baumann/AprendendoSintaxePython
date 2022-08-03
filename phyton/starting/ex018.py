import numpy as np
from sklearn import linear_model

def calculadoraProbabilidade(var, X):
    chanceReg = regressaoLogistica.coef_ * X + regressaoLogistica.intercept_
    chance = np.exp(chanceReg)
    probabilidade = chance /(1 + chance)
    return probabilidade

X = np.array([12,33,45,17,21,36]).reshape(-1,1)
y = np.array([0,1,1,0,0,1])

regressaoLogistica = linear_model.LogisticRegression()
regressaoLogistica.fit(X,y)

print(calculadoraProbabilidade(regressaoLogistica, X))