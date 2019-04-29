from tkinter import Tk, YES, BOTH, Button, Canvas, Image

import model
import PIL
from PIL import ImageDraw, Image
import numpy as np

model = model.model()
# model.my_model.load_weights("88.6.h5")
# model.my_model.load_weights("89.1.h5")
# model.train(4112, 1, 5e-4)


class drawWindow:
    def __init__(self):
        self.drawWindow = Tk()
        global lastx, lasty
        lastx, lasty = None, None
        self.cv = Canvas(self.drawWindow, width=300, height=300, bg='white')
        # --- PIL
        self.image1 = PIL.Image.new('RGB', (300, 300), "black")
        self.draw = ImageDraw.Draw(self.image1)

        self.cv.bind('<1>', self.activate_paint)
        self.cv.pack(expand=YES, fill=BOTH)

        self.btn_save = Button(self.drawWindow, text="save", command=self.save)
        self.btn_save.pack()
        self.drawWindow.mainloop()

    def process_img(self, img):
        img = img.resize((28, 28), Image.ANTIALIAS)
        img.save("newImg.png")
        img = np.array(img)
        img = img[:, :, 0]
        print(img.shape)
        img = img.reshape(1, 28, 28, 1)
        return img

    def save(self):
        self.drawWindow.destroy()
        filename = 'image.png'  # image_number increments by 1 at every save
        self.image1.save(filename)
        img = Image.open(filename)
        img = self.process_img(img)
        idx = model.predict(img)
        print(idx)
        showImage = Image.open('letters/' + str(idx) + '.png')
        showImage.show()

    def activate_paint(self, e):
        global lastx, lasty
        self.cv.bind('<B1-Motion>', self.paint)
        lastx, lasty = e.x, e.y

    def paint(self, e):
        global lastx, lasty
        x, y = e.x, e.y
        self.cv.create_line((lastx, lasty, x, y), width=35)
        #  --- PIL
        self.draw.line((lastx, lasty, x, y), fill='white', width=35)
        lastx, lasty = x, y
