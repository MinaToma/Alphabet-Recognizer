import numpy as np
from tensorflow.contrib.learn.python.learn.datasets.mnist import extract_images, extract_labels
from PIL import Image
import PIL


def load_data():
    trainI = 'dataset/data/emnist-letters-train-images-idx3-ubyte.gz'
    trainL = 'dataset/data/emnist-letters-train-labels-idx1-ubyte.gz'

    testI = 'dataset/data/emnist-letters-test-images-idx3-ubyte.gz'
    testL = 'dataset/data/emnist-letters-test-labels-idx1-ubyte.gz'

    with open(trainI, 'rb') as f:
        train_images = extract_images(f)
    with open(trainL, 'rb') as f:
        train_label = extract_labels(f)

    with open(testI, 'rb') as f:
        test_images = extract_images(f)
    with open(testL, 'rb') as f:
        test_label = extract_labels(f)

    numOFtrain = train_images.shape[0]
    numOFtest = test_images.shape[0]

    train_images = train_images.reshape(numOFtrain, 28, 28)
    train_label = train_label.reshape(numOFtrain, 1)

    test_images = test_images.reshape(numOFtest, 28, 28)
    test_label = test_label.reshape(numOFtest, 1)

    train_images1 = []
    test_images1 = []

    for i in range(numOFtrain):
        temp = train_images[i]
        temp = PIL.Image.fromarray(np.uint8(temp))
        temp = temp.transpose(Image.FLIP_LEFT_RIGHT)
        temp = temp.rotate(90)
        temp = np.array(temp)

        train_images1.append(temp)

    for i in range(numOFtest):
        temp = test_images[i]
        temp = PIL.Image.fromarray(np.uint8(temp))
        temp = temp.transpose(Image.FLIP_LEFT_RIGHT)
        temp = temp.rotate(90)
        temp = np.array(temp)
        test_images1.append(temp)

    train_images1 = np.array(train_images1)
    train_images1 = train_images1.reshape(numOFtrain, 28, 28, 1)

    test_images1 = np.array(test_images1)
    test_images1 = test_images1.reshape(numOFtest, 28, 28, 1)

    return train_images1, train_label, test_images1, test_label
