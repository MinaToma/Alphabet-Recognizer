from tkinter import *

from PIL import Image
import drawWindow

welcomeWindow = Tk()
mainWindow = Tk()
mainWindow.withdraw()


def predict():
    drawWindow.drawWindow()


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

welcomeWindow.mainloop()
