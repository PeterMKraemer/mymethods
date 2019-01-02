#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
                                computations
-------------------------------------------------------------------------------
This module contains simple computations that come handy for data description.
===============================================================================
Created on Wed Jan  2 09:00:52 2019

@author: peterkraemer
"""
import numpy as np


# binAvg is a function that calculates means and variablity for specified bins.
# input variables:      data:       expected to be a pandas data frame
#                       bins:       need to be specified manually
#                       xVar:       column name of independent variable, which bins accord to
#                       yVar:       column name of dependent variable
#                       breakVar:   column name of breaker variable
#
# output variable:      means:      matrix containing mean yVar and variability for individual bins

def binAvg(data,bins,xVar,yVar,breakVar='subjID'):
    binsize = np.unique(np.diff(bins,1))
    means = np.zeros(shape = (len(bins),5)) # 1st column = means of bin, 2nd column = SD, 3nd column = SEM, 4th column = 95% CIs

    for i in np.arange(len(bins)):
        #select data within bin
        idxVal = data.index[(data[xVar] >= bins[i]-binsize[0]/2) & (data[xVar] < bins[i]+binsize[0]/2)].tolist()
        dataBin = data.loc[idxVal]
        
        #get means on one level (e.g. subject specific means)
        meansBin = dataBin.groupby([breakVar])[yVar].mean()
        
        #calculate binned average
        means[i][0] = np.average(meansBin)
        
        #calculate standard deviation
        means[i][1] = np.std(meansBin)
        
        #calculate standard error
        means[i][2] = means[i][1]/np.sqrt(len(meansBin))
        
        #calculate 95% confidence intervals, assuming normally distributed data and independence of samples
        means[i][3] = means[i][2]*2 # lower bar
        means[i][4] = means[i][2]*2 # upper bar
    return means
