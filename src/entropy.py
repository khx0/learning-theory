#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: nikolas.schnellbaecher@bioquant.uni-heidelberg.de
# date: 2018-05-29
# file: entropy.py
##########################################################################################

import math
import numpy as np
    
def checkPDFnorm(PDF, xGrid, textString = '', verbose = False):
    norm = np.trapz(PDF, xGrid)
    print("norm(" + textString + ") =", norm)
    if (not np.isclose(norm, 1.0)):
        print(textString + " distribution seems NOT to be normalized to 1.")
        if (verbose):
            sys.exit(1)
                        
def getSampleEntropy(sample):
    entropy = 0.0
    for i, x in enumerate(sample):
        if (np.isclose(x, 0.0)):
            entropy += 0.0
        else:
            entropy += x * np.log2(x)
    return -1.0 * entropy

if __name__ == '__main__':

    pass


