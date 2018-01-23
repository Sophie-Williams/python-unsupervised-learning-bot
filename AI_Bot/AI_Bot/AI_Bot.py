#per modificare la schermata in input presa dal gioco
import cv2
#per prendere la schermata dal gioco
from PIL import ImageGrab
#per trasformare l'immagine in un array
import numpy as np
#per visualizzare i frame
import time

import json

import Species as s

from scipy import misc

import utils

import conv_model as cm

import pyautogui

import os.path

import GraphDrawer as gd


#def processImg(imgToProcess):
#    processedImg = cv2.cvtColor(imgToProcess,cv2.COLOR_RGB2GRAY)
#    return processedImg

model = cm.getModel()

#cm.trainModel(model,
#              'path_validation',
#              'path_training',
#              'destination_tensorboard_log',
#              'destination_conv_weights')

#cm.loadWeights(model,'path_weights')

X = 12
Y = 10

#IA param
maxGenomes = 3
currentGenome = 0
currentIteration = 0
fitness = 0
 
#IA Init
specie = s.Species(maxGenomes,-1,12,3,[40,5,2])

batch_size = 32

totalGenomes = 0

graph = gd.GraphDrawer('Generation','Fitness')

cm.loadWeights(model,'D:/Projects/giovani ricercatori cercansi/AI_Bot/AI_Bot/weights/pesi_finale.h5')

#serialization
if(os.path.isfile('D:/Projects/giovani ricercatori cercansi/AI_Bot/AI_Bot/nnWeights.npy')):
    specie.setWeights(np.load('D:/Projects/giovani ricercatori cercansi/AI_Bot/AI_Bot/nnWeights.npy'))
    print('Weights loaded succesfully!')


isGameOver = True
ultimoFrame = time.time()

# 0 --> still
# 1 --> left
# 2 --> right
prevDirection = 0

while(True):
    screen = ImageGrab.grab(bbox=(41,158,800,600))
    screen = misc.imresize(screen,(60,80))
    screen = np.array(screen)
    screen = utils.swapArray(screen)
    #print(screen)
    #cv2.imshow('eiiii',screen)
    np.moveaxis(screen,0,-1).shape
    screen = np.expand_dims(screen,axis=0)
    #print(model.predict(screen,batch_size=batch_size)[0][0])
    if(cm.predictInput(model,screen)[0][0] < 0.5):
        if(not isGameOver):
            isGameOver = True
            specie.setFitness(currentGenome,fitness)
            print('Fitness: ' + str(fitness))
            specie.nextGeneration()
            if(currentGenome >= maxGenomes - 1):
                currentGenome = 0
                currentIteration = currentIteration + 1
                np.save('D:/Projects/giovani ricercatori cercansi/AI_Bot/AI_Bot/nnWeights.npy',specie.getWeights())
                print('\nfm: ' + str(specie.getMediumFitness()))
                graph.addPoint(currentIteration,specie.getMediumFitness())
                print('Weights saved succesfully!')
            else:
                currentGenome = currentGenome + 1
                totalGenomes = totalGenomes + 1
                print('\n\nGenome: ' + str(currentGenome) + '\nGeneration: ' + str(currentIteration));

        fitness = 0
        pyautogui.keyUp('left')
        pyautogui.keyUp('right')
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        time.sleep(5)
        #print("HOPERSOOOOOO")

    else:
        isGameOver = False
        #print(specie.toString())
        specie.feedGenome(currentGenome,utils.genInput(X,Y,screen))                 
        output = specie.getOutputs(currentGenome)
        #print(currentGenome)
        #print(specie.toString())
        print(output)

        if(output[0] > 0.5):
            pyautogui.keyDown('left')
            print("left")
            if(prevDirection != 1):
                prevDirection = 1
                fitness = fitness + 3
        else:
            pyautogui.keyUp('left')

        if(output[1] > 0.5):
            pyautogui.keyDown('right')
            print("right")
            if(prevDirection != 2):
                prevDirection = 2
                fitness = fitness + 3
        else:
            pyautogui.keyUp('right')

        if((output[0] > 0.5) & (output[1] < 0.5)):
            if(prevDirection != 1):
                prevDirection = 1
                fitness = fitness + 3
        elif((output[0] > 0.5) & (output[1] < 0.5)):
            if(prevDirection != 1):
                prevDirection = 1
                fitness = fitness + 3
        elif(((output[0] > 0.5) & (output[1] > 0.5)) | ((output[0] < 0.5) & (output[1] < 0.5))):
            if(prevDirection != 0):
                prevDirection = 0
                fitness = fitness + 3

        fitness = fitness + 1
    #print(time.time()-ultimoFrame)
    ultimoFrame = time.time()

    if(totalGenomes == 6000):
        utils.saveWeights(specie,0,'destination_weights')
        break;
    
