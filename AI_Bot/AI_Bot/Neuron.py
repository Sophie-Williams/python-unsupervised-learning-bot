import random
import math
import numpy as np
class Neuron(object):
    """description of class"""

    output=0
    weights=[]

    def __init__(self,params):
        if isinstance(params,int):
            self.defaultConstructor(params)
        elif isinstance(params,Neuron): 
            self.copyConstructor(params)
        else:
            self.weigthConstructor(params)

    def defaultConstructor(self,nInputs):
        self.weights= np.empty(nInputs,dtype=object)
        self.randomWeights()

    def weigthConstructor(self,weights):
        self.weights=weights
        i=0
        while i < len(weights):
            self.weights[i]=weights[i]
            i+=1
    
    def copyConstructor(self,neuronToCopy):
        i=0
        while i < len(neuronToCopy.weights):
            self.weights[i]=neuronToCopy.weights[i]
            i+=1
      
    def calculateOutput(self,inputs):
        sum = self.weightedSum(inputs)
        self.activationFunction(sum)
    
    def weightedSum(self,inputs):
        toRtn = 0
        i = 0
        while i < len(self.weights):
            #print(len(self.weights))
            toRtn += inputs[i]*self.weights[i]
            i += 1
        return toRtn

    def activationFunction(self,sumToActivate):
        self.output = 1/(1 + math.exp(-sumToActivate))

    def getOutput(self):
        return self.output

    def getWeights(self):
        return self.weights

    def setWeights(self,weights):
        self.weights = weights
        

    def randomWeights(self):
        #for weight in self.weights:
        #    weight = random.uniform(-1,1)
        i = 0
        while i < len(self.weights):
            self.weights[i] = random.uniform(-1,1)
            i+=1


    def toString(self):
        toRtn = "° neuron:\n"
        i = 0

        while i < len(self.weights):
            toRtn += "w" + str(i) + ": " + str(self.weights[i]) + "\n"
            i+=1

        return toRtn;

    




