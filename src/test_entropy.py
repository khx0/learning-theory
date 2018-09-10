#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-09-10
# file: test_entropy.py
##########################################################################################

import sys
import os
import numpy as np
import unittest

from entropy import getSampleEntropy

class entropy_test(unittest.TestCase):
    
    """
    Test cases for the entropy module.
    """
    
    def test_getSampleEntropy_01(self):
    
        probs = np.array([0.5, 0.5])
        entropy = getSampleEntropy(probs)
        refEntropy = 1.0
        self.assertTrue(np.isclose(entropy, refEntropy))
        
        probs = np.array([1.0, 0.0])
        entropy = getSampleEntropy(probs)
        refEntropy = 0.0
        self.assertTrue(np.isclose(entropy, refEntropy))
        
        probs = np.array([0.0, 1.0])
        entropy = getSampleEntropy(probs)
        refEntropy = 0.0
        self.assertTrue(np.isclose(entropy, refEntropy))
        
        probs = np.array([0.5, 0.25, 0.25])
        entropy = getSampleEntropy(probs)
        refEntropy = 1.5
        self.assertTrue(np.isclose(entropy, refEntropy))
        
        probs = np.array([0.25, 0.5, 0.25])
        entropy = getSampleEntropy(probs)
        refEntropy = 1.5
        self.assertTrue(np.isclose(entropy, refEntropy))
        
        probs = np.array([0.25, 0.25, 0.5])
        entropy = getSampleEntropy(probs)
        refEntropy = 1.5
        self.assertTrue(np.isclose(entropy, refEntropy))
        
        probs = np.array([0.5, 0.5, 0.0])
        entropy = getSampleEntropy(probs)
        refEntropy = 1.0
        self.assertTrue(np.isclose(entropy, refEntropy))
        
        probs = np.array([0.5, 0.0, 0.5])
        entropy = getSampleEntropy(probs)
        refEntropy = 1.0
        self.assertTrue(np.isclose(entropy, refEntropy))

        probs = np.array([0.0, 0.5, 0.5])
        entropy = getSampleEntropy(probs)
        refEntropy = 1.0
        self.assertTrue(np.isclose(entropy, refEntropy))
        
        probs = np.array([1.0/3.0, 1.0/3.0, 1.0/3.0])
        entropy = getSampleEntropy(probs)
        refEntropy = 1.584962501
        self.assertTrue(np.isclose(entropy, refEntropy))
        
        return None
        
if __name__ == '__main__':
    
    unittest.main()

    
    
    
    
