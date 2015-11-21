# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:33:38 2015

@author: bastian
"""

from random import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pylab

class Rect:
    def __init__(self, x_low, y_low, x_high, y_high):
        self.x_low = x_low
        self.x_high = x_high
        self.y_low = y_low
        self.y_high = y_high
        
    def classify_points(self, points):
        result = []
        for point in points:
            if ((point[0] >= self.x_low) and (point[0] <= self.x_high) and (point[1] >= self.y_low) and (point[1] <= self.y_high)):
                result.append(Point(point[0], point[1], 1))
            else:
                result.append(Point(point[0], point[1], 0))
        return result
        
class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

def create_random_point(lower_bound, upper_bound):
    return randint(lower_bound, upper_bound)
    
    
def create_random_rectangle():
    x = []
    y = []
    x.append(create_random_point(0, 100))
    x.append(create_random_point(0, 100))
    y.append(create_random_point(0, 100))
    y.append(create_random_point(0, 100))
    
    if x[0] < x[1]:
        x_low = x[0]
        x_high = x[1]
    else:
        x_low = x[1]
        x_high = x[0]
    if y[0] < y[1]:
        y_low = y[0]
        y_high = y[1]
    else:
        y_low = y[1]
        y_high = y[0]
    
    return Rect(x_low, y_low, x_high, y_high)
    
def create_uniformly_distributed_points(number_of_points):
    result = []
    for i in range(number_of_points):
        result.append((create_random_point(0,100), create_random_point(0,100)))     
    return result

def create_rectangles(number_of_rectangles):
    result = []
    for i in range(number_of_rectangles):
        result.append(create_random_rectangle())
    return result
    
def add_rectangle_to_plot(axis, rectangle):
    axis.add_patch(
        patches.Rectangle(
            ((rectangle.x_high - rectangle.x_low) / 2, (rectangle.y_high - rectangle.y_low) / 2),
            rectangle.x_high - rectangle.x_low,
            rectangle.y_high - rectangle.y_low,
            alpha = 0.1
            )
        )

def classify_random_points_with_random_rectangles(rectangles, number_of_points_per_rectangle): 
    classified_points = []
    for rectangle in rectangles:
        points = create_uniformly_distributed_points(number_of_points_per_rectangle)
        classified_points.extend(rectangle.classify_points(points))
    return classified_points


rectangles = create_rectangles(15)
classified_points = classify_random_points_with_random_rectangles(rectangles, 50)
fig1 = plt.figure()

ax1 = fig1.add_subplot(111, aspect='equal')

for rectangle in rectangles:
    add_rectangle_to_plot(ax1, rectangle)
#print classified_points
for point in classified_points:
    #print point
    if point.value == 1:
        ax1.plot(point.x, point.y, 'r+')
    else:
        ax1.plot(point.x, point.y, 'b.')

pylab.ylim([0,100])
pylab.xlim([0,100])

pylab.savefig('ex3.jpg')