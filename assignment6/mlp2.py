# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:03:39 2015

@author: bastian
"""
import numpy as np

f = lambda x : 1 / ( 1 + np.exp(-x))
f_d = lambda x : f(x) * (1 - f(x))

class MLP:
    
    def __init__(self, initial_weights):
        # input to hidden
        self.w31 = initial_weights
        self.w41 = initial_weights
        self.w32 = initial_weights
        self.w42 = initial_weights
        # hidden to output
        self.w53 = initial_weights
        self.w54 = initial_weights
        # bias
        self.w30 = initial_weights
        self.w40 = initial_weights
        self.w50 = initial_weights
    
    def propagate(self, net_input):
        # input
        self.output_1 = net_input[0]
        self.output_2 = net_input[1]
        
        # hidden
        self.input_3 = self.w30+self.w31*self.output_1 + self.w32*self.output_2
        self.output_3 = f(self.input_3)
        self.input_4 = self.w40 + self.w41*self.output_1 + self.w42*self.output_2
        self.output_4 = f(self.input_4)
        
        #output
        self.input_5 = self.w50+self.w53*self.output_3 + self.w54*self.output_4
        self.output_5 = f(self.input_5)
        
        return self.output_5
        
    def backpropagate(self, net_input, desired_output, learning_rate):
        net_output = self.propagate(net_input)
        error = desired_output - net_output
        
        self.delta_5 = f_d(self.input_5) * error
        self.delta_4 = f_d(self.input_4) * self.w54 * self.delta_5
        self.delta_3 = f_d(self.input_3) * self.w53 * self.delta_5

        self.w50 = self.w50 + learning_rate*self.delta_5
        self.w53 = self.w53 + learning_rate*self.delta_5*self.output_3
        self.w54 = self.w54 + learning_rate*self.delta_5*self.output_4
        
        self.w40 = self.w40 + learning_rate * self.delta_4
        self.w42 = self.w42 + learning_rate * self.delta_4*self.output_2
        self.w41 = self.w41 + learning_rate * self.delta_4*self.output_1
        
        self.w30 = self.w30 + learning_rate * self.delta_3
        self.w32 = self.w32 + learning_rate * self.delta_3*self.output_2
        self.w31 = self.w31 + learning_rate * self.delta_3*self.output_1

    
mlp = MLP(0.5)
print mlp.propagate((1,1))
mlp.backpropagate((1,1),0.01, 0.1)

learning_rate = 0.1
for i in range(1000):
    mlp.backpropagate((1,1), 0.01, learning_rate)
    mlp.backpropagate((0,1), 0.99, learning_rate)
    mlp.backpropagate((1,0), 0.99, learning_rate)
    mlp.backpropagate((0,0), 0.01, learning_rate)
print mlp.propagate((0,0))
print mlp.propagate((1,0))
print mlp.propagate((0,1))
print mlp.propagate((1,1))