import tkinter as tk
from tkinter import font
from tkinter import * 
import requests 
from tkintermapview import TkinterMapView
from tkinter.ttk import Combobox
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfile
from tkinter import filedialog as fd
from PIL import ImageTk, Image  

HEIGHT = 800
WIDTH = 600   

root = tk.Tk()

# setting up opening page
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = '#E2D4BA')
canvas.pack()

title = Label(canvas, text = "MyPhotoWizard", font = ('Courier',45,"bold"),bg = '#E2D4BA',fg = '#AF7A6D')
title.place(relx = 0.5, rely =0.04, anchor = 'n')

button = tk.Button(root, text = 'Select File', command = lambda:upload_file())
button.place(relx=0.5, rely = 0.15, anchor = 'n')

# function for accessing file
def upload_file():
    frame = tk.Frame(root, bg = '#E2D4BA')
    frame.pack()
    frame.place(relx = 0.5, rely = 0.235, anchor = 'n')

    filename = fd.askopenfilename(title = 'Select an image file')
    filename = Image.open(filename)
    resized = filename.resize((350,250))
    photo = ImageTk.PhotoImage(resized)

    label = tk.Label(frame, image = photo)
    label.pack()

    root.mainloop()


root.mainloop()





