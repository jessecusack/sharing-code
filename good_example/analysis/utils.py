"""Miscellaneous functions for processing VMP data."""

import numpy as _np


def despike_threshold(x, x_max=1):
    """Replaces bad values of buoyancy frequency squared with NaN using a threshold.
    
    Parameters
    ----------
        x : array_like
            Data to be despiked.
        x_max : float, optional
            Maximum data value. Default is 1.
            
    Returns
    -------
        x_clean : ndarray
            Despiked data.
    
    """
    x_clean = _np.asarray(x).copy()
    x_clean[x_clean > x_max] = _np.NaN
    return x_clean


def calculate_diffusivity(eps, N2, gamma=0.2):
    """Estimate the turbulent diffusivity from dissipation and stratification.
    
    Parameters
    ----------
        eps : array_like
            Turbulent dissipation rate of kinetic energy [W kg-1].
        N2 : array_like
            Buoyancy frequency squared (angular units e.g. radians) [s-2].
        gamma : float, optional
            Flux coefficient (sometimes called the mixing efficiency) [-].
            
    Returns
    -------
        Krho : ndarray
            Turbulent diffusivity [m2 s-1]
    
    """
    
    Krho = gamma * _np.asarray(eps) / _np.asarray(N2)
    return Krho


def convolve_hanning(x, win=5):
    """Smooth data by convolving a hanning function of length 'win'."""
    w = _np.hanning(win)
    return _np.convolve(x, w, mode="same") / w.sum()
