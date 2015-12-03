# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:42:49 2015

@author: bastian
"""

import numpy as np
import sklearn.svm.libsvm
import random
from matplotlib import pyplot as plt


RADIUS = 10
WIDTH = 6
VERTICAL_SEPARATION = 5

def sample_upper_halfmoon(radius, width):
    distance = random.random() * width + radius - 0.5 * width
    angle = random.random() * 180
    angle = np.radians(angle)
    x = np.cos(angle) * distance
    y = np.sin(angle) * distance
    return x,y
    
def sample_lower_halfmoon(radius, width, vertical_separation):
    distance = random.random() * width + radius - 0.5 * width
    angle = random.random() * 180 + 180
    angle = np.radians(angle)
    x = np.cos(angle) * distance + radius
    y = np.sin(angle) * distance - vertical_separation
    return x,y
    
def sample_pair(radius, width, vertical_separation):
    upper_sample = sample_upper_halfmoon(radius, width)
    lower_sample = sample_lower_halfmoon(radius, width, vertical_separation)
    return [upper_sample, lower_sample]

def get_x_y_values(data):
    x = []
    y = []
    for point in data:
        x.append(point[0])
        y.append(point[1])
    return x,y
    
training_sample = []
test_sample = []
for i in range(1000):
    training_sample.append(sample_pair(RADIUS, WIDTH, VERTICAL_SEPARATION))
    
for i in range(3000):
    test_sample.append(sample_pair(RADIUS, WIDTH, VERTICAL_SEPARATION))
    
x,y = get_x_y_values(training_sample)
fig = plt.figure()
plt.title('variances of cluster 6')    
ax = fig.add_subplot(111)
ax.scatter(x, y) 

print training_sample[0]
