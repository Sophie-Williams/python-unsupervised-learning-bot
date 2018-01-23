import Layer
import random
import numpy as np
class Genome(object):
    """description of class"""
    fitness = 0
    layers= []

    def __init__(self,params):
        if len(params) == 1:
            self.copyConstructor(params[0])
        elif len(params) == 2:
            self.childConstructor(params[0],params[1])
        else:
            self.defaultConstructor(params[0],params[1],params[2])
    
    def defaultConstructor(self,nInputs,nLayers,topology):
        self.layers=np.empty(nLayers,dtype=object)
        self.fitness=0
        self.initLayers(nInputs,topology)
    

    def copyConstructor(self,toCopy):
        self.layers = self.neurons = np.empty(len(toCopy.layers),dtype=object)
        i=0
        while(i<len(toCopy.layers)):
            self.layers[i]=toCopy.layers[i]
            i+=1
        self.fitness=toCopy.fitness;


    def childConstructor(self,parent1,parent2):
        p1w = parent1.getWeights()
        p2w = parent2.getWeights()
        cw = np.empty(len(p1w),dtype=object)

        percentage= random.random()
        tmpPercentage = 0
        cont = 0

        i = 0
        while i < len(p1w):
            cw[i] = np.empty(len(p1w[i]),dtype=object)
            j = 0

            while j < len(p1w[i]):
                cw[i][j] = np.empty(len(p1w[i][j]),dtype=object)
                k = 0

                while k < len(p1w[i][j]):
                    tmpPercentage = random.uniform(0,1);
                    if tmpPercentage < percentage:
                        cw[i][j][k] = p1w[i][j][k]
                    else:
                        cw[i][j][k] = p2w[i][j][k]

                    cont += 1
                    k += 1

                j += 1

            i += 1

        #mutation
        cw = self.mutate(cw,cont)

        #creation of the new genome
        self.fitness = 0
        self.layers = np.empty(len(parent1.layers),dtype=object)
        i = 0
        while i < len(self.layers):
            self.layers[i] = Layer.Layer([cw[i]])
            i += 1


    def mutate(self,w,nWeights):
        percentage = 1/nWeights
        tmpPercentage = 0

        for wLayer in w:
            for wNeuron in wLayer:
                for weight in wNeuron:
                    tmpPercentage = random.uniform(0,1)
                    if tmpPercentage < percentage:
                        weight = random.uniform(-1,1)
        return w


    def getWeights(self):
        toRtn=np.empty(len(self.layers),dtype=object)
        i=0
        while(i<len(self.layers)):
            toRtn[i]=self.layers[i].getWeights()
            i+=1

        return toRtn


    def setWeights(self,weights):
        i = 0
        while i < len(self.layers):
            self.layers[i].setWeights(weights[i])
            i += 1
        

    def initLayers(self,nInputs,topology):
        self.layers[0]= Layer.Layer([topology[0],nInputs])
        i=1
        #print(len(self.layers))
        while(i<len(self.layers)):
            print(i)
            self.layers[i]= Layer.Layer([topology[i],topology[i-1]])
            i+=1


    def feedNetwork(self,inputs):
        self.layers[0].calculateOutputs(inputs)

        i = 1
        while i < len(self.layers):
            self.layers[i].calculateOutputs(self.layers[i-1].getOutputs())
            i += 1

    def getOutputs(self):
        return self.layers[len(self.layers) - 1].getOutputs()


    def setFitness(self,fitness):
        self.fitness = fitness


    def getFitness(self):
        return self.fitness


    def toString(self):
        toRtn = "°genome: \n"
        tmp = self.getOutputs()
        i = 0

        while i < len(self.layers):
            toRtn += str(i+1) + self.layers[i].toString()
            i+=1

        toRtn += "Final outputs: "
        i = 0

        while i < len(tmp):
            toRtn += str(tmp[i]) + " ";
            i+=1

        return toRtn;

