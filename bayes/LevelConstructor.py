import pandas as pd
import numpy as np


def LevelConstructor(data, breakerVariable):
    ll = np.zeros(len(data))
    idx, mem = 1, 1
    for i, dataidx in enumerate(data.index):
        if mem != data[breakerVariable][dataidx]:
            idx += 1
            mem = data[breakerVariable][dataidx]
        ll[i] = idx
    return ll