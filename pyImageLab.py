# -*- encoding: utf-8 -*-

import os, sys
from tkinter import*
import tkinter.filedialog
import tkinter.colorchooser
import math
from copy import copy
from PIL import Image, ImageTk,ImageFilter,ImageOps
      



class userInterfaze:
    window_size= "640x480"      #Tamaño de la ventana del programa.
    size = 256, 256             #Tamaño de las miniaturas de las imágenes.
    color = "grey"
    filters = {'Ocultar en Bit menos sig'}      #ComboBox: Métodos de esteganografía
    acImage = ''
    outImage = ''
    def __init__(self, master):
        global actlmage
        global outImage
        self.master = master
        master.title("steganographyLab")

        
        tkvar = StringVar(root)
        tkvar.set('Ocultar en Bit menos sig')
        master.geometry(self.window_size)
        self.window = tkinter.Frame(master)
        self.window.pack()
        
        inImage = Image.open("Imagenes/intro.jpg")                      #Abrir Imagen por defecto de la entrada.
        actlmage = copy(inImage)
        outImage = copy(inImage)
        inImage.thumbnail(self.size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
        self.tkimage = ImageTk.PhotoImage(inImage)			#Mostrar imagen
        self.inMiniaturePanel = tkinter.Label(self.window, image=self.tkimage,width=256,height=256)
        self.inMiniaturePanel.grid(row=0)

        outputimage = Image.open("Imagenes/result.jpg")			#Abrir Imagen por defecto de la salida.
        outputimage.thumbnail(self.size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
        self.tkimageout = ImageTk.PhotoImage(outputimage)
        outMiniaturePanel = tkinter.Label(self.window, image=self.tkimageout,width=256,height=256)
        outMiniaturePanel.grid(row=0,column=2)

        chooseButton = tkinter.Button(self.window,text="Selecionar Imagen",command=self.chooseImage).grid(row=1,column=0,pady=8)      #Botón de carga de imágenes
        saveButton = tkinter.Button(self.window,text="Guadar Imagen",command=self.saveImage).grid(row=1,column=2)                     #Botón para guardar imágenes

        Label(self.window,text="Seleccione filtro: ").grid(row=2,column=0)
        filterMenu = OptionMenu(self.window,tkvar,*self.filters).grid(row=2,column=1)                                                 #ComboBox
        filerButton = tkinter.Button(self.window,text="Aplicar Filtro").grid(row=2,column=2,pady= 30)         #Botón que aplica el filtro seleccionado por el ComboBox
            
    # Método que se utiliza para cargar una imagen al programa.
    def chooseImage(self):
        global actlmage
        filename =tkinter.filedialog.askopenfilename()
        inImage2 = Image.open(filename)				#Abrir Imagen
        actlmage = copy(inImage2)
        self.refreshImages(inImage2,self.inMiniaturePanel)
   
    #Método encargado de guardar la imagen procesada.
    def saveImage(self):
        global outImage
        savefile = tkinter.filedialog.asksaveasfile(mode='w',defaultextension=".jpg")
        if savefile:    #Comprueba si se le dío a cancelar.
            outImage.save(savefile)

    #Método encargado de aplicar los filtros.
    def aplyFilter():
        global actlmage
        global outImage
        auxiliarImg = copy(actlmage)
       #NOW HERE STEGANOGRAPHI METHOD
        outImage=copy(showIm)
        self.refreshImages(showIm,outMiniaturePanel)

    #Método que refresca miniaturas.   
    def refreshImages(self,newMiniatureImage,panel):
        newMiniatureImage.thumbnail(self.size, Image.ANTIALIAS)
        tkimageout = ImageTk.PhotoImage(newMiniatureImage)			#Mostrar imagen
        panel.configure(image = tkimageout)
        panel.image = tkimageout
    
root = tkinter.Tk()            
ui = userInterfaze(root)
root.mainloop()
