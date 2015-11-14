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
        for i in range(number_input):
            self.input_neurons.append(InputNeuron())
        
        self.bias = BiasNeuron()
        
        # create hidden layer
        for i in range(number_hidden):
            hidden_neuron = Neuron()
            self.hidden_neurons.append(hidden_neuron)
            # add connections to input layer
            for input_neuron in self.input_neurons:
                connection = Connection(input_neuron, hidden_neuron, initial_weight)
                hidden_neuron.add_incomming_connection(connection)
                input_neuron.add_outgoing_connection(connection)
            # add BIAS connection
            connection = Connection(self.bias, hidden_neuron, initial_weight)
            hidden_neuron.add_incomming_connection(connection)
            self.bias.add_outgoing_connection(connection)
            
        # create output layer
        for i in range(number_output):
            output_neuron = Neuron()
            self.output_neurons.append(output_neuron)
            # add connections to hidden layer
            for hidden_neuron in self.hidden_neurons:
                connection = Connection(hidden_neuron, output_neuron, initial_weight)
                output_neuron.add_incomming_connection(connection)
                hidden_neuron.add_outgoing_connection(connection)
            # add BIAS connection
            connection = Connection(self.bias, output_neuron, initial_weight)
            output_neuron.add_incomming_connection(connection)
            self.bias.add_outgoing_connection(connection)
                
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
            for connection in neuron.outgoing_connections:
                if(not queue.__contains__(connection.target_neuron)):
                    queue.append(connection.target_neuron)
            index += 1
          
        # get output
        result = []
        for output in self.output_neurons:
            result.append(output.last_output)
        return result
        
    def backpropagate(self, net_input, desired, learning_rate):
        self.propagate(net_input)        
        
        # compute delta for output neurons
        for i in range(len(desired)):
            neuron = self.output_neurons[i]
            error = neuron.last_output - desired[i]
            neuron.last_delta = neuron.derive(neuron.last_induced_local_field) * error
            
        queue = []
        for output in self.output_neurons:
            for incomming in output.incomming_connections:
                queue.append(incomming.start_neuron)
        
        index = 0
        while(index < len(queue)):
            neuron = queue[index]
            #compute outgoing weight change and delta
            error_sum = 0            
            for outgoing in neuron.outgoing_connections:
                error_sum += outgoing.target_neuron.last_delta * outgoing.weight
                delta_weight = learning_rate*outgoing.target_neuron.last_delta*neuron.last_output
                #print "weight change: ", delta_weight
                outgoing.set_weight(outgoing.weight + delta_weight)
                #print "new weight: ", outgoing.weight
            neuron.last_delta = neuron.derive(neuron.last_induced_local_field) * error_sum
            #add incoming neurons
            for incomming in neuron.incomming_connections:
                if(not queue.__contains__(incomming.start_neuron)):
                    queue.append(incomming.start_neuron)
            index += 1
            
    def __str__(self):
        result = "Input Layer: "
        for neuron in self.input_neurons:
            result += "\nNeuron connections: "
            for connection in neuron.outgoing_connections:
                result += "\n" + str(connection.weight)
        result += "\nHidden Layer: "
        for neuron in self.hidden_neurons:
            result += "\nNeuron connections: "
            for connection in neuron.outgoing_connections:
                result += "\n" + str(connection.weight)
        result += "\nOutput Layer: "
        for neuron in self.output_neurons:
            result += "\nNeuron connections: "
            for connection in neuron.outgoing_connections:
                result += "\n" + str(connection.weight)
        return result

class Neuron:
    
    last_induced_local_field = 0
    last_output = 0
    last_delta = 0
    incomming_connections = []
    outgoing_connections = []
      
    
    def compute_induced_local_field(self):
        induced_local_field = 0
        for connection in self.incomming_connections:
            activation = connection.start_neuron.last_output
            induced_local_field += activation * connection.weight
        self.last_induced_local_field = induced_local_field
        return self.last_induced_local_field
        
    def derive(self, value):
        f = lambda x : 1 / (1 + np.exp((-1) * x)) 
        y = f(value)
        return y * (1 - y)

    def activate(self):
        self.last_output = 1 / (1 + np.exp((-1) * self.last_induced_local_field))
        return self.last_output
        
    def set_delta(self, delta):
        self.last_delta = delta
        
    def set_last_output(self, output):
        self.last_output = output
        
    def add_incomming_connection(self, incomming_connection):
        self.incomming_connections.append(incomming_connection)
    
    def add_outgoing_connection(self, outgoing_connection):
        self.outgoing_connections.append(outgoing_connection)
        
    #def __str__(self):
     #   result = "Incomming connections: "
      #  for connection in self.incomming_connections:
       #     result += str(connection)
        #result += "\nOutgoing connections: "
        #for connection in self.outgoing_connections:
        #    result += str(connection)
        #return result
        
        
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
        

class Connection:
    def __init__(self, start_neuron, target_neuron, weight):
        self.start_neuron = start_neuron
        self.target_neuron = target_neuron
        self.weight = weight
        
    def set_weight(self, weight):
        self.weight = weight
        
    #def __str__(self):
     #   return "Start: " + str(self.start_neuron) + "Target: " + str(self.target_neuron) + "Weight: " + str(self.weight)

mlp = MLP(1,1,1,0.5)
#print mlp.input_neurons[0].incomming_connections