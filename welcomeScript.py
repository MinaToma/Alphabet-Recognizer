from tkinter import *

from tensorflow.contrib.learn.python.learn.datasets.mnist import extract_images
import numpy as np
import model
import tensorflow as tf
import PIL
from PIL import Image, ImageDraw
from skimage import io, color
model = model.model()
model.my_model.load_weights("83.3.h5")
# model.train(4112, 1, 5e-4)

welcomeWindow = Tk()
drawWindow = Tk()
drawWindow.withdraw()
mainWindow = Tk()
mainWindow.withdraw()


def process_img(img):
    img = img.resize((28, 28), Image.ANTIALIAS)
    img.save("h.png")
    img = color.rgb2lab(img)

    img = np.array(img)
    img = img[:, :, 0]
    print(img.shape)
    img = img.reshape(1, 28, 28, 1)
    return img

def predict():
    drawWindow.deiconify()


def show_loss():
    img = Image.open('LOSS.png')
    img.show()


def show_accuracy():
    img = Image.open('ACC.png')
    img.show()


def back_main():
    mainWindow.withdraw()
    welcomeWindow.deiconify()


def openMainWindow():
    welcomeWindow.withdraw()
    mainWindow.deiconify()


# /---------------------------------------------------------------------------------------------------------------------/

welcomeWindow.geometry("500x500")

welcome = Label(welcomeWindow, text="Welcome To Character Recognition", fg="blue")
welcome.pack(side=TOP, fill=X)

mainWindowButton = Button(welcomeWindow, text="Start", command=openMainWindow)
mainWindowButton.pack()

# /---------------------------------------------------------------------------------------------------------------------/

mainWindow.geometry("500x500")
predictButton = Button(mainWindow, text="Predict", command=predict)
predictButton.pack()

showLoss = Button(mainWindow, text="Loss", command=show_loss)
showLoss.pack()

showAccuracy = Button(mainWindow, text="Accuracy", command=show_accuracy)
showAccuracy.pack()

backButton = Button(mainWindow, text="back", command=back_main)
backButton.pack()


# /---------------------------------------------------------------------------------------------------------------------/

def save():
    cv.delete(image1)
    drawWindow.withdraw()
    filename = 'image.png'  # image_number increments by 1 at every save
    image1.save(filename)
    img = Image.open(filename)
    img = process_img(img)
    idx = model.predict(img)
    print(idx)
    showImage = Image.open('letters/' + str(idx) + '.png')
    showImage.show()


def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), width=8)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='black', width=8)
    lastx, lasty = x, y


lastx, lasty = None, None
cv = Canvas(drawWindow, width=700, height=700, bg='white')
# --- PIL
image1 = PIL.Image.new('RGB', (560, 560), 'white')
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)

btn_save = Button(drawWindow, text="save", command=save)
btn_save.pack()

# /---------------------------------------------------------------------------------------------------------------------/

welcomeWindow.mainloop()
