# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:36:41 2015

@author: bastian
"""

import random
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


RADIUS = 10
WIDTH = 6
VERTICAL_SEPARATION = 0

class Pair:
    def __init__(self, pair_a, pair_b):
        self.pair_a = pair_a
        self.pair_b = pair_b

def sample_upper_halfmoon(radius, width):
    distance = random.random() * width + radius - 0.5 * width
    angle = random.random() * 180
    angle = np.radians(angle)
    x = np.cos(angle) * distance
    y = np.sin(angle) * distance
    return [x,y]
    
def sample_lower_halfmoon(radius, width, vertical_separation):
    distance = random.random() * width + radius - 0.5 * width
    angle = random.random() * 180 + 180
    angle = np.radians(angle)
    x = np.cos(angle) * distance + radius
    y = np.sin(angle) * distance - vertical_separation
    return [x,y]
    
def sample_pair(radius, width, vertical_separation):
    pair_a = sample_upper_halfmoon(radius, width)
    pair_b = sample_lower_halfmoon(radius, width, vertical_separation)
    
    return Pair(pair_a, pair_b)
    
training_samples = []
for i in range(1000):
    training_samples.append(sample_pair(RADIUS,WIDTH, VERTICAL_SEPARATION))
    
test_samples = []
for i in range(3000):
    test_samples.append(sample_pair(RADIUS,WIDTH, VERTICAL_SEPARATION))
    
figure = plt.figure()
for sample in training_samples:
    ax = figure.add_subplot(111)
    ax.plot(sample.pair_a[0], sample.pair_a[1], 'ro')
    ax.plot(sample.pair_b[0], sample.pair_b[1], 'bo')