from copy import copy

import numpy as np

from tentmap.map import Gn

def create_dist_data(*,
                     x0s = np.linspace(0, 1, 50),
                     As = np.linspace(1, 2, 50),
                     N = 100):
    Amap = []
    for A in As:
        xs = []
        for x0 in x0s:
            xs.append(Gn(x0, 100, A=A))
        Amap.append(xs)
    return np.array(Amap) # array[Avalue, Xvalue]


def get_data_anal(*,
                     x0s = np.linspace(0, 1, 50),
                     As = np.linspace(1, 2, 50),
                     N = 100):
    data = create_dist_data(x0s=x0s, As=As, N=N)
    data_counts = np.zeros((
            len(As),
            len(x0s)
        ))

    # iter A-values
    for (i, A) in enumerate(As):
        X_res = data[i, :]
        X_counts = np.zeros(len(x0s))

        #iter results
        for x in X_res:
            #iter x[i], x[i+1]
            for (j, (xi, xi1)) in enumerate(zip(x0s[:-1], x0s[1:])):
                if x >= xi and x < xi1:
                    X_counts[j] += 1

        data_counts[i, :] = X_counts/np.linalg.norm(X_counts)
    return data_counts

