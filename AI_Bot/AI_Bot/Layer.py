import Neuron
import numpy as np
class Layer(object):
    """description of class"""
    neurons = None

    def __init__(self, params):
        if len(params) == 1:
            self.weightConstructor(params[0])
        else:
            self.defaultConstructor(params[0],params[1])

    
    def defaultConstructor(self,nNeurons,nInputs):
        self.neurons = np.empty(nNeurons,dtype=object)
        #print("nNeur:" + str(len(self.neurons)))
        self.initNeurons(nInputs)

    def weightConstructor(self, weights):
        i = 0
        self.neurons = np.empty(len(weights),dtype=object)
        #print("nNeur:" + str(len(self.neurons)))
        while i < len(self.neurons):
            self.neurons[i] = Neuron.Neuron(weights[i])
            i+=1

    def initNeurons(self,nInputs):
        i = 0
        while i < len(self.neurons):
            self.neurons[i] = Neuron.Neuron(nInputs)
            i+=1

    def calculateOutputs(self,inputs):
        for neur in self.neurons:
            neur.calculateOutput(inputs)

    def calculateOutputs(self,inputs):
        i = 0

        if not isinstance(inputs[0],float):
            #n inputs for each neuron
            while i < len(self.neurons):
                self.neurons[i].calculateOutput(inputs[i])
                i+=1
        else:
            #all inputs for each neuron
            while i < len(self.neurons):
                self.neurons[i].calculateOutput(inputs)
                i+=1

    def getNumNeurons(self):
        return len(self.neurons)

    def getOutput(self,i):
        return self.neurons[i].getOutput()

    def getOutputs(self):
        toRtn = np.empty(len(self.neurons),dtype=object)
        i = 0
        while i < len(self.neurons):
            toRtn[i] = self.getOutput(i)
            i += 1
        
        return toRtn

    def getWeights(self):
        toRtn = np.empty(len(self.neurons),dtype=object)
        i = 0
        while i < len(self.neurons):
            toRtn[i] = self.neurons[i].getWeights()
            i += 1

        return toRtn


    def setWeights(self,weights):
        i = 0
        while i < len(self.neurons):
            self.neurons[i].setWeights(weights[i])
            i+=1


    def toString(self):
        toRtn = "°layer: \n"
        i = 0

        while i < len(self.neurons):
            toRtn += str(i+1) + self.neurons[i].toString()
            i += 1

        return toRtn;


