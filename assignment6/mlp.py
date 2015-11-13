# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:32:20 2015

@author: bastian
"""

import numpy as np

class MLP:
    
    input_neurons = []
    output_neurons = []
    hidden_neurons = []
    
    def __init__(self, number_input, number_hidden, number_output, initial_weight):
        print "Constructor of MLP not yet implemented"
        for i in range(number_input):
            self.input_neurons.append(InputNeuron())
        
        self.bias = BiasNeuron()
        
        # create hidden layer
        for i in range(number_hidden):
            hidden_neuron = Neuron()
            self.hidden_neurons.append(hidden_neuron)
            # add connections to input layer
            for input_neuron in self.input_neurons:
                hidden_neuron.add_incomming_neuron([input_neuron, initial_weight])
                input_neuron.add_outgoing_neuron(hidden_neuron)
            # add BIAS connection
            hidden_neuron.add_incomming_neuron([self.bias, initial_weight])
            self.bias.add_outgoing_neuron(hidden_neuron)
            
        # create output layer
        for i in range(number_output):
            output_neuron = Neuron()
            self.output_neurons.append(output_neuron)
            # add connections to hidden layer
            for hidden_neuron in self.hidden_neurons:
                output_neuron.add_incomming_neuron([hidden_neuron, initial_weight])
                hidden_neuron.add_outgoing_neuron(output_neuron)
            # add BIAS connection
            output_neuron.add_incomming_neuron([self.bias, initial_weight])
            self.bias.add_outgoing_neuron(output_neuron)
                
    def propagate(self, net_input):
        
        for i in range(len(net_input)):
            self.input_neurons[i].set_last_output(net_input[i])

        queue = []            
        for hidden in self.hidden_neurons:
            queue.append(hidden)
        
        index = 0
        while(index < len(queue)):
            neuron = queue[index]
            neuron.compute_induced_local_field()
            neuron.activate()
            for outgoing in neuron.outgoing_neurons:
                if(not queue.__contains__(outgoing)):
                    queue.append(outgoing)
            index += 1
          
        # get output
        result = []
        for output in self.output_neurons:
            result.append(output.last_output)
        return result
        
    def backpropagate(self, desired):
        
            

class Neuron:
    
    last_induced_local_field = 0
    last_output = 0
    last_delta = 0
    incomming_neurons = []
    outgoing_neurons = []
    
    def compute_induced_local_field(self):
        induced_local_field = 0
        for connection in self.incomming_neurons:
            activation = connection[0].last_output
            induced_local_field += activation * connection[1]
        self.last_induced_local_field = induced_local_field
        return self.last_induced_local_field

    def activate(self):
        self.last_output = 1 / (1 + np.exp((-1) * self.last_induced_local_field))
        return self.last_output
        
    def set_delta(self, delta):
        self.last_delta = delta
        
    def set_last_output(self, output):
        self.last_output = output
        
    def add_incomming_neuron(self, incomming_neuron):
        self.incomming_neurons.append(incomming_neuron)
    
    def add_outgoing_neuron(self, outgoing_neuron):
        self.outgoing_neurons.append(outgoing_neuron)
        
        
class InputNeuron(Neuron):
    
    def activate(self):
        return self.last_output
        
    def compute_induced_local_field(self):
        return self.last_induced_local_field
        
class BiasNeuron(Neuron):
    
    def __init__(self):
        self.last_output = 1
        
    def activate(self):
        return 1
        

mlp = MLP(2,2,1,0)
print "input neurons: ", mlp.input_neurons
print "hidden neurons: ", mlp.hidden_neurons
print "output neurons: ", mlp.output_neurons

print "Propagate 1,1: ", mlp.propagate((0,0))