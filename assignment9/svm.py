# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:36:41 2015

@author: bastian
"""

import random
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.svm import *

RADIUS = 10
WIDTH = 6
VERTICAL_SEPARATION = 0

# TODO: SVM is supervised -> assign labels according to part of upper or lower half moon

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
    a = sample_upper_halfmoon(radius, width)
    b = sample_lower_halfmoon(radius, width, vertical_separation)
    return a,b
    
def plot_points_with_specified_separaration(vertical_separation):
    training_samples_x = []
    training_samples_y = []
    training_class = []
    for i in range(1000):
        a,b = sample_pair(RADIUS,WIDTH, vertical_separation)
        training_samples_x.append(a[0])
        training_samples_x.append(b[0])
        training_samples_y.append(a[1])
        training_samples_y.append(b[1])
        training_class.append(-1)
        training_class.append(1)
        
    test_samples_x = []
    test_samples_y = []
    test_class = []
    for i in range(3000):
        a,b = sample_pair(RADIUS,WIDTH, vertical_separation)
        test_samples_x.append(a[0])
        test_samples_x.append(b[0])
        test_samples_y.append(a[1])
        test_samples_y.append(b[1])
        test_class.append(-1)
        test_class.append(1)
        
    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.scatter(test_samples_x, test_samples_y, c=np.array(test_class).astype(np.float))
    return  training_samples_x, training_samples_y, training_class, test_samples_x, test_samples_y, test_class



def fit_and_predict(samples, kernel_type):
    training = np.array([samples[0], samples[1]], dtype='float64').T
    clf = SVC(kernel=kernel_type).fit(training, np.array(samples[2], dtype='float64'))
    prediction = clf.predict(np.array([samples[3],samples[4]], dtype='float64').T)
    fig1 = plt.figure()
    plt.title(kernel_type)
    ax1 = fig1.add_subplot(111)
    ax1.scatter(samples[3],samples[4], c=prediction.astype(np.float))

set1=plot_points_with_specified_separaration(0)
set2=plot_points_with_specified_separaration((-1) * (RADIUS-0.5*WIDTH))
set3=plot_points_with_specified_separaration((-1) * (RADIUS+0.5*WIDTH))

fit_and_predict(set1, 'linear')
fit_and_predict(set2, 'linear')
fit_and_predict(set3, 'linear')

fit_and_predict(set1, 'rbf')
fit_and_predict(set2, 'rbf')
fit_and_predict(set3, 'rbf')

#fit_and_predict(set1, 'poly')
#fit_and_predict(set2, 'poly')
#fit_and_predict(set3, 'poly')

#fit_and_predict(set1, 'sigmoid')
#fit_and_predict(set2, 'sigmoid')
#fit_and_predict(set3, 'sigmoid')

