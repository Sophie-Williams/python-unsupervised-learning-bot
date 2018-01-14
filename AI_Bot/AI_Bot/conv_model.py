
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
#functions
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import optimizers
from keras import backend as K
from keras import callbacks as call
import h5py

def getModel():
    
    model = Sequential()
    model.add(Conv2D(32,(3,3), input_shape =(3,60,80)))
    model.add(Activation('sigmoid'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(32,(3,3)))
    model.add(Activation('sigmoid'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(64,(3,3)))
    model.add(Activation('sigmoid'))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('sigmoid'))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])

    return model

def predictInput(model,input):
    return model.predict(input)

def loadWeights(model,path):
    model.load_weights(path)



def trainModel(model,validation_path,training_path,tensorboard_path,weights_path):

    train_datagen = ImageDataGenerator()

    test_datagen = ImageDataGenerator()

    train_generator = train_datagen.flow_from_directory(
        training_path,
        target_size = (60,80),
        batch_size=32,
        class_mode='binary')

    validation_generator = test_datagen.flow_from_directory(
        validation_path,
        target_size=(60,80),
        batch_size=32,
        class_mode='binary')

    if(tensorboard_path != None):
        tb = call.TensorBoard(log_dir=tensorboard_path, histogram_freq=0, write_graph=True, write_images=True)

        model.fit_generator(
            train_generator,
            steps_per_epoch=2000 // 32,
            epochs=50,
            validation_data=validation_generator,
            validation_steps=800//32,
            callbacks=[tb])
    else:
        model.fit_generator(
            train_generator,
            steps_per_epoch=2000 // 32,
            epochs=50,
            validation_data=validation_generator,
            validation_steps=800//32,)

    model.save_weights(weights_path)

def evaluateModel(model,weights_path,input_path):
    model.load_weights(weights_path)

    model.summary()

    predictions_dir = input_path

    predictions = []

    for file in glob.glob(predictions_dir+"*.jpeg"):
        with Image.open(file) as image:
            image = img_to_array(image)
            image = np.expand_dims(image,axis=0)
            predictions.append(image)

    i = 0

    for file in predictions:
        print(str(i))
        print(model.predict(file,batch_size=128))