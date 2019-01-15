#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:14:55 2019

@author: peterkraemer
"""
import numpy as np

def HDIofMCMC(sampleVec, credMass=.95):
  # Computes highest density interval from a sample of representative values,
  #   estimated as shortest credible interval.
  # Arguments:
  #   sampleVec
  #     is a vector of representative values from a probability distribution.
  #   credMass
  #     is a scalar between 0 and 1, indicating the mass within the credible
  #     interval that is to be estimated.
  # Value:
  #   HDIlim is a vector containing the limits of the HDI
  # © John Kruschke https://stats.stackexchange.com/questions/252988/highest-density-interval-in-stan
    sortedPts = np.sort(sampleVec)
    ciIdxInc = int(np.ceil(credMass*len(sortedPts)))
    nCIs = len(sortedPts) - ciIdxInc
    ciWidth=np.zeros(nCIs)
    for i in np.arange(nCIs):
        ciWidth[i]=sortedPts[i+ciIdxInc]-sortedPts[i]
    HDImin = sortedPts[np.argmin(ciWidth)]
    HDImax = sortedPts[np.argmin(ciWidth) + ciIdxInc]
    HDIlim = np.array([HDImin,HDImax])
    return HDIlim