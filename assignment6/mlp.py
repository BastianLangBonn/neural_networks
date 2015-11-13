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

        # propagate through hidden layer
        self.hidden_induced_fields = []
        self.hidden_output = []
        for i in range(len(self.hidden_layer)):
            # compute input to hidden layer
            # BIAS
            induced_local_field = self.input_hidden_weights[i][0]
            for j in range(len(net_input) ):
                induced_local_field += net_input[j] * self.input_hidden_weights[i][j+1]
            self.hidden_induced_fields.append(induced_local_field)
            # compute output of hidden layer
            self.hidden_output.append(self.hidden_layer[i].compute_output(induced_local_field))
        
        # propagate through output layer
        self.output_induced_fields = []
        self.output_output = []
        for i in range(len(self.output_layer)):
            #BIAS
            induced_local_field = self.hidden_output_weights[i][0]
            for j in range(len(self.hidden_output)):
                induced_local_field += self.hidden_output[j] * self.hidden_output_weights[i][j+1]
            self.output_induced_fields.append(induced_local_field)
            self.output_output.append(self.output_layer[i].compute_output(induced_local_field))
        
        return self.output_output
        
    def backprop(self, input_vector, desired_output, learning_rate):
        # Compute output error
        output_vector = self.propagate_input(input_vector)
        output_errors = []
        for i in range(len(output_vector)):
            output_errors.append(output_vector[i] - desired_output[i])
        print "error: ", output_errors
                
        # Compute output delta
        delta_output = []
        for i in range(len(output_errors)):
            derivative = self.output_layer[i].derivative_activation(self.output_induced_fields[i])
            delta_output.append(derivative * output_errors[i])
        print "delta output: ", delta_output
            
        # Compute hidden delta
        delta_hidden = []
        for i in range(len(self.hidden_output_weights)):
            

            
class Neuron:
    def compute_output(self, induced_local_field):
        return 1 / (1 + np.exp((-1) * induced_local_field))
        
    def derivative_activation(self, induced_local_field):
        return self.compute_output(induced_local_field) * (1 - self.compute_output(induced_local_field))
        
        
mlp = MLP(2, 2, 1, 0)
print "input-hidden weights", mlp.input_hidden_weights
print "hidden-output weights", mlp.hidden_output_weights
#print mlp.input_hidden_weights
print mlp.propagate_input([1,1])

mlp2 = MLP(2, 2, 1, 0.5)
print "input-hidden weights", mlp2.input_hidden_weights
print "hidden-output weights", mlp2.hidden_output_weights
print mlp2.propagate_input([1,1])

mlp.backprop([1,1], [0], 0.2)

