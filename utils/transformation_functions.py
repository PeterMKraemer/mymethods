import numpy as np

def SoftPlus(x):
    y = np.log(1+np.exp(x))
    return y
def SoftPlusInv(x):
    y = np.log(np.exp(x) - 1.)
    return y
def Z(x):
    z = (x - np.mean(x)) / np.std(x)
    return z