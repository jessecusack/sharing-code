import numpy as np

def despike(x, x_max=1):
    x_clean = np.asarray(x).copy()
    x_clean[x_clean > x_max] = np.NaN
    return x_clean

def diff(eps, N2, gamma=0.2):
    Krho = gamma * np.asarray(eps) / np.asarray(N2)
    return Krho

def smooth(x, win=5):
    w = np.hanning(win)
    return np.convolve(x, w, mode='same') / w.sum()
