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

labelFont = font.Font(family='Helvetica', size=30, weight='bold', slant='italic')
welcome = Label(welcomeWindow, text="Welcome To\nCharacter Recognition", font=labelFont, fg="#7da1c1").place(x=40, y=110)

mainWindowButton = Button(welcomeWindow, text="Start", command=openMainWindow, width=35, height=2, bg="#232323",
                          fg="white").place(x=95, y=355)

# /---------------------------------------------------------------------------------------------------------------------/

buttonFont = font.Font(family='Helvetica', size=40, weight='bold', slant='italic')

mainWindow.geometry("500x500")
predictButton = Button(mainWindow, text="Predict", command=predict, bg="#7da1c1", fg="black", font=buttonFont)
predictButton.place(bordermode=OUTSIDE, height=225, width=250, x=0, y=0)

testButton = Button(mainWindow, text="Test", command=show_loss, bg="#eaea60", fg="black", font=buttonFont)
testButton.place(bordermode=OUTSIDE, height=225, width=250, x=250, y=0)

showLoss = Button(mainWindow, text="Loss", command=show_loss, bg="#ff5b5b", fg="black", font=buttonFont)
showLoss.place(bordermode=OUTSIDE, height=225, width=250, x=0, y=225)

showAccuracy = Button(mainWindow, text="Accuracy", command=show_accuracy, bg="#b5ff5b", fg="black", font=buttonFont)
showAccuracy.place(bordermode=OUTSIDE, height=225, width=250, x=250, y=225)

backButton = Button(mainWindow, text="BACK", command=back_main, bg="#232323", fg="white", font=buttonFont)
backButton.place(bordermode=OUTSIDE, height=50, width=500, x=0, y=450)

# /---------------------------------------------------------------------------------------------------------------------/

welcomeWindow.mainloop()
