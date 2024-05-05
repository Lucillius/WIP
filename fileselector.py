import numpy
import tkinter
#import pytorch
#import tensorflow
#import scipy
#import pybrain
#import pandas
#import matplotlib
from tkinter import filedialog as fileDialog
from tkinter.messagebox import showinfo as showInfo
#Requests an image file from the user
window = tkinter.Tk()
window.title("Tkinter open file dialog")
window.resizable(False, False)
window.geometry("300x150")
#defining file types that are compatible
def select_file():
    filetypes = (
        ("jpg files", ".jpg")
        ("png files", ".png")
        (".jpeg files", ".jpeg")
        (".tif files", ".tif")
        (".xcf files", ".xcf")
    )
    fileNames = fileDialog.askopenfilename(
        title = "open a file"
        #initialdir = "/"
    )
    showInfo(
        title = "selected files"
        #message = fileNames
    )