# import tensorflow as tf
# config = tf.ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.30
# session = tf.Session(config=config)
from keras.models import model_from_yaml
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy
import numpy as np
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D, Conv2DTranspose
from keras import optimizers
from keras.layers.normalization import BatchNormalization
from keras.layers import Activation, Flatten, Dense
from keras.regularizers import l2
import data



class model:
    def __init__(self):
        # self.trainI, self.trianL, self.testI, self.testL = data.load_data()
        self.my_model = self.moodel()

    def moodel(self):
        reg = 0
        model = Sequential()

        model.add(Convolution2D(16, (6, 6), padding='same', strides=(2, 2), input_shape=(28, 28, 1),
                                activity_regularizer=l2(reg)))
        model.add(BatchNormalization(axis=-1))
        model.add(Activation('relu'))

        model.add(Convolution2D(8, (3, 3), padding='same', strides=(2, 2), activity_regularizer=l2(reg)))
        model.add(BatchNormalization(axis=-1))
        model.add(Activation('relu'))

        model.add(Convolution2D(4, (2, 2), padding='same', strides=(2, 2), activity_regularizer=l2(reg)))
        model.add(BatchNormalization(axis=-1))
        model.add(Activation('relu'))

        model.add(Flatten())

        model.add(Dense(8))
        model.add(Activation('relu'))
        model.add(Dense(4))
        model.add(Activation('relu'))
        model.add(Dense(27, activation='softmax'))

        return model

    def train(self, batch_size, epochs, learning_rate):
        self.my_model.summary()

        self.adam = optimizers.adam(lr=learning_rate)
        # self.RMS = optimizers.RMSprop(lr=learning_rate)

        self.my_model.compile(loss='sparse_categorical_crossentropy', optimizer=self.adam, metrics=['accuracy'])

        history = self.my_model.fit(self.trainI, self.trianL, batch_size=batch_size, epochs=epochs, shuffle=True,
                                    validation_split=0.2)

        self.plot_history(history)

        self.my_model.save_weights('weights.h5')

        model_yaml = self.my_model.to_yaml()
        with open("model.yaml", "w") as yaml_file:
            yaml_file.write(model_yaml)

    def evaluate(self):
        self.adam = optimizers.adam(lr=5e-3)
        # self.RMS = optimizers.RMSprop(lr=5e-3)

        self.my_model.compile(loss='sparse_categorical_crossentropy', optimizer=self.adam, metrics=['accuracy'])

        hist = self.my_model.evaluate(self.testI, self.testL, batch_size=2056)
        print(hist)
        # self.plot_history(hist)

    def predict(self, x):
        y = self.my_model.predict(x)
        y = np.argmax(y)
        return y

    def plot_history(self, history):
        # list all data in history
        print(history.history.keys())
        # summarize history for accuracy
        plt.plot(history.history['acc'])
        plt.plot(history.history['val_acc'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
        # summarize history for loss
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
