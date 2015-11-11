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
        self.create_layer(self.hidden_layer, number_hidden)
        self.create_layer(self.output_layer, number_output)
        self.input_hidden_weights = self.create_weights(number_input, number_hidden, initial_weight_value)
        self.hidden_output_weights = self.create_weights(number_hidden, number_output, initial_weight_value)
    
    def create_weights(self, number_origin_layer, number_target_layer, initial_weight_value):
        weight_matrix = []
        for i in range(number_origin_layer):
            weights = []
            #BIAS
            weights.append(initial_weight_value)
            for j in range(number_target_layer):
                weights.append(initial_weight_value)
            weight_matrix.append(weights)
        return weight_matrix
            
    def create_layer(self, layer, number_of_neurons):
        for i in range(number_of_neurons):
            layer.append(Neuron())
            
    def propagate_input(self, net_input):
        print "net input:", net_input
        hidden_output = []
                
        for i in range(len(self.hidden_layer)):
            # compute input to hidden layer
            # BIAS
            induced_local_field = self.input_hidden_weights[i][0]
            for j in range(len(net_input)):
                induced_local_field += net_input[j] * self.input_hidden_weights[j][i+1]
            # compute output of hidden layer
            print "induced_local_field:", induced_local_field
            hidden_output.append(self.hidden_layer[i].compute_output(induced_local_field))
        
        print "hidden_output:", hidden_output
        output_output = []
        for i in range(len(self.output_layer)):
            #BIAS
            induced_local_field = self.hidden_output_weights[i][0]
            for j in range(len(hidden_output)):
                induced_local_field += hidden_output[j] * self.hidden_output_weights[j][i+1]
            #output_induced_field.append(induced_local_field)
            output_output.append(self.output_layer[i].compute_output(induced_local_field))
        
        return output_output
            
            
class Neuron:
    def compute_output(self, induced_local_field):
        return 1 / (1 + np.exp((-1) * induced_local_field))
        
        
mlp = MLP(2, 2, 1, 0)
print "input-hidden layer", mlp.input_hidden_weights
print "hidden-output layer", mlp.hidden_output_weights
#print mlp.input_hidden_weights
print mlp.propagate_input([1,1])

