# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:32:20 2015

@author: bastian
"""

import numpy as np

class MLP:
    
    hidden_layer = []
    output_layer = []
    input_hidden_weights = []
    hidden_output_weights = []
    
    def __init__(self, number_input, number_hidden, number_output, initial_weight_value):
        self.number_of_inputs = number_input
        self.hidden_layer = self.create_layer(number_hidden)
        self.output_layer = self.create_layer(number_output)
        self.input_hidden_weights = self.create_weights(number_input, number_hidden, initial_weight_value)
        self.hidden_output_weights = self.create_weights(number_hidden, number_output, initial_weight_value)
        
    
    def create_weights(self, number_origin_layer, number_target_layer, initial_weight_value):
        weight_matrix = []
        for i in range(number_target_layer):
            weights = []
            #BIAS
            weights.append(initial_weight_value)
            for j in range(number_origin_layer):
                weights.append(initial_weight_value)
            weight_matrix.append(weights)
        return weight_matrix
            
    def create_layer(self, number_of_neurons):
        result = []
        for i in range(number_of_neurons):
            result.append(Neuron())
        return result            
            
    def propagate_input(self, net_input):
        hidden_output = []
        for i in range(len(self.hidden_layer)):
            # compute input to hidden layer
            # BIAS
            induced_local_field = self.input_hidden_weights[i][0]
            for j in range(len(net_input) ):
                induced_local_field += net_input[j] * self.input_hidden_weights[i][j+1]
            # compute output of hidden layer
            hidden_output.append(self.hidden_layer[i].compute_output(induced_local_field))
        
        output_output = []
        for i in range(len(self.output_layer)):
            #BIAS
            induced_local_field = self.hidden_output_weights[i][0]
            for j in range(len(hidden_output)):
                induced_local_field += hidden_output[j] * self.hidden_output_weights[i][j+1]
            #output_induced_field.append(induced_local_field)
            output_output.append(self.output_layer[i].compute_output(induced_local_field))
        
        return output_output
            
            
class Neuron:
    def compute_output(self, induced_local_field):
        return 1 / (1 + np.exp((-1) * induced_local_field))
        
        
mlp = MLP(2, 2, 1, 0)
print "input-hidden weights", mlp.input_hidden_weights
print "hidden-output weights", mlp.hidden_output_weights
#print mlp.input_hidden_weights
print mlp.propagate_input([1,1])

mlp2 = MLP(2, 2, 1, 0.5)
print "input-hidden weights", mlp2.input_hidden_weights
print "hidden-output weights", mlp2.hidden_output_weights
print mlp2.propagate_input([1,1])

