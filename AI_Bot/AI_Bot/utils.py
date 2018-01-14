
import numpy as np
import json
import codecs

def genInput(X,Y,screenPixels):

    #print(screenPixels[0][0][0])
    inputs = np.empty(shape=(400),dtype=object)

    index = 0
    jndex = 0

    ylength = 80/Y
    xlength = 60/X

    input_count = 0
    while(index < xlength):
        jndex = 0
        while(jndex < ylength):
            arraytmp = np.empty(shape=(X*Y),dtype=object)
            count = 0
            xndex = index * X
            yndex = jndex * Y
            while(xndex < ((index * X) + X)):
                yndex = jndex * Y
                while(yndex < ((jndex * Y) + Y)):
                    arraytmp[count] = (screenPixels[0,0,xndex,yndex] + screenPixels[0,1,xndex,yndex] + screenPixels[0,2,xndex,yndex]) / 30
                    count = count + 1
                    yndex = yndex + 1
                xndex = xndex + 1
            inputs[input_count] = arraytmp;
            input_count = input_count + 1
            jndex = jndex + 1
        index = index + 1

    return inputs

def swapArray(screen):
    index = 0
    toRtn = np.zeros((3,60,80))
    while(index < len(screen)):
        jndex = 0
        while(jndex < len(screen[index])):
            kindex = 0
            while(kindex < len(screen[index,jndex])):
                toRtn[kindex,index,jndex] = screen[index,jndex,kindex]
                kindex = kindex + 1
            jndex = jndex + 1
        index = index + 1
    return toRtn

def saveWeights(specie,nGenome,file_path):
    toSave = specie.getWeights()
    toSave = toSave.tolist()
    json.dump(toSave, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)

def loadWeights(file_path,specie):
    obj_text = codecs.open(file_path, 'r', encoding='utf-8').read()
    weights = json.loads(obj_text)
    weights = np.array(weights)
    specie.setWeights(weights)
