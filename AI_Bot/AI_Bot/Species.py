import Genome
import numpy as np
class Species(object):
    """description of class"""

    INFINITE_ITERATIONS = -1
    genomes = []
    iterations = 0
    currentIterations = 0

    def __init__(self,nGenomes,iterations,nInputs,nLayers,topology):
        self.genomes = np.empty(nGenomes,dtype=object)
        self.iterations = iterations
        self.currentIterations = 1
        
        self.initSpecies(nInputs,nLayers,topology)


    def initSpecies(self,nInputs,nLayers,topology):
        i = 0
        while i < len(self.genomes):
            self.genomes[i] = Genome.Genome([nInputs,nLayers,topology])
            i+=1


    def setFitness(self,nGenome,fitness):
        self.genomes[nGenome].setFitness(fitness)


    def nextGeneration(self):
        if (self.currentIterations <= self.iterations):
            self.reorder()
            self.makeChildren()
            self.currentIterations += 1


    def makeChildren(self):
        i = 2
        while i < len(self.genomes):
            self.genomes[i] = Genome.Genome(self.genomes[0],self.genomes[1])
            i += 1


    def reorder(self):
        i = 2
        while i < len(self.genomes):
            if self.genomes[i].getFitness() > self.genomes[0].getFitness():
                self.genomes[0] = Genome.Genome(self.genomes[i])
            elif self.genomes[i].getFitness() > self.genomes[1].getFitness():
                self.genomes[1] = Genome.Genome(self.genomes[i])

            i += 1


    def getWeights(self,nGenome):
        return self.genomes[nGenome].getWeights()


    def getWeights(self):
        weights = np.empty(len(self.genomes),dtype=object)
        i = 0
        while i < len(self.genomes):
            weights[i] = self.genomes[i].getWeights()
            i += 1
        return weights


    def setWeights(self,weights):
        i = 0
        while i < len(self.genomes):
            self.genomes[i].setWeights(weights[i])
            i += 1


    def getCurrentIteration(self):
        return self.currentIterations


    def feedGenome(self,nGenome,inputs):
        self.genomes[nGenome].feedNetwork(inputs)


    def getOutputs(self,nGenome):
        return self.genomes[nGenome].getOutputs()


    def toString(self):
        toRtn = "Species (iteration: " + str(self.currentIterations) + ")\n"
        i = 0

        while i < len(self.genomes):
            toRtn += str(i+1) + self.genomes[i].toString() + "\n"
            i+=1

        return toRtn

    def getMediumFitness(self):
        i = 0
        totFitness = 0
        nGenomes = len(self.genomes)

        while i < nGenomes:
            totFitness += self.genomes[i].getFitness()
            i += 1

        return totFitness/nGenomes

