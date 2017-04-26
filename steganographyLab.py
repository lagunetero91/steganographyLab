# -*- encoding: utf-8 -*-

import os, sys
from tkinter import*
from tkinter import messagebox
import tkinter.filedialog
import tkinter.colorchooser
import math
from copy import copy
from PIL import Image, ImageTk,ImageFilter,ImageOps
import binascii

class userInterfaze:
    window_size= "800x600"      #Tamaño de la ventana del programa.
    size = 256, 256             #Tamaño de las miniaturas de las imágenes.
    color = "grey"
    filters = {'Bit menos significativo'}      #ComboBox: Métodos de esteganografía
    acImage = ''
    outImage = ''
    file = 0
    def __init__(self, master):
        global actlmage
        global outImage
        self.master = master
        master.title("steganographyLab")

        
        tkvar = StringVar(root)
        tkvar.set('Bit menos significativo')
        master.geometry(self.window_size)
        master. resizable(width=False, height=False)
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
        self.outMiniaturePanel = tkinter.Label(self.window, image=self.tkimageout,width=256,height=256)
        self.outMiniaturePanel.grid(row=0,column=2)

        chooseButton = tkinter.Button(self.window,text="Selecionar Imagen",command=self.chooseImage).grid(row=1,column=0,pady=8)      #Botón de carga de imágenes
        saveButton = tkinter.Button(self.window,text="Guadar Imagen",command=self.saveImage).grid(row=1,column=2)                     #Botón para guardar imágenes

        Label(self.window,text="Esteganografía: ").grid(row=2,column=0)
        filterMenu = OptionMenu(self.window,tkvar,*self.filters).grid(row=2,column=1)                                                 #ComboBox
        filerButton = tkinter.Button(self.window,text="Aplicar",command=self.aplySteganography).grid(row=2,column=2,pady= 20)         #Botón que aplica el filtro seleccionado por el ComboBox

        chooseTextButton = tkinter.Button(self.window,text="Fichero con Texto",command=self.chooseText).grid(row=3,column=0)
        self.filepatch= Entry(self.window,width=30)
        self.filepatch.grid(row=3,column=1,pady=30)
        
        textIn = Text(height=5)
        textIn.insert(END,"Introduzca el texto a aplicar a la Esteganografía ...")
        textIn.pack()
        
    # Método que se utiliza para cargar una imagen al programa.
    def chooseImage(self):
        global actlmage
        filename =tkinter.filedialog.askopenfilename()
        if filename:
            try:
                inImage2 = Image.open(filename)				#Abrir Imagen
                actlmage = copy(inImage2)
                self.refreshImages(inImage2,self.inMiniaturePanel)
            except:
                tkinter.messagebox.showerror("Error","Fallo al abrir el archivo.")
                
    #Método encargado de guardar la imagen procesada.
    def saveImage(self):
        global outImage
        savefile = tkinter.filedialog.asksaveasfile(mode='w',defaultextension=".jpg")
        if savefile:    #Comprueba si se le dío a cancelar.
            try:
                outImage.save(savefile)
            except:
                messagebox.showerror("Error","Fallo al abrir el archivo")


    #Método encargado de aplicar los filtros.
    def aplySteganography(self):
        global actlmage
        global outImage
        auxiliarImg = copy(actlmage)
       #NOW HERE STEGANOGRAPHI METHOD
        self.lessBit(actlmage,self.file)
        showIm = auxiliarImg
        outImage=copy(showIm)
        self.refreshImages(showIm,self.outMiniaturePanel)

    #Método que refresca miniaturas.   
    def refreshImages(self,newMiniatureImage,panel):
        newMiniatureImage.thumbnail(self.size, Image.ANTIALIAS)
        tkimageout = ImageTk.PhotoImage(newMiniatureImage)			#Mostrar imagen
        panel.configure(image = tkimageout)
        panel.image = tkimageout

    def chooseText(self):
        filename =tkinter.filedialog.askopenfilename()
        if filename:
            try:
                self.filepatch.insert(10,filename)
                self.file = open(filename,'r')
            except:
                messagebox.showerror("Error","Fallo al abrir el archivo")

    def lessBit(self,image,fText):
        width,height = image.size
        maxLetters = width*height*3
        message = fText.read()
        print(message)
        binMessage = bin(int.from_bytes(message.encode(),'big'))
        print(binMessage)
        if maxLetters < len(binMessage):
            return 0
        charNum = 0
        for i in range(width):
            for j in range(height):
                r,g,b = image.getpixel((i,j))
                if (r % 2 == 1) and (binMessage[charNum]==0):
                    print(charNum)
                    r=r-1
                elif (r % 2 == 0) and (binMessage[charNum]==1):
                    r=r+1
                    print(charNum)
                charNum=charNum+1
                if charNum>=len(binMessage):
                   return image
                if (g % 2 == 1) and (binMessage[charNum]==0):
                    g=g-1
                    print(charNum)
                elif (g % 2 == 0) and (binMessage[charNum]==1):
                    g=g+1
                    print(charNum)
                charNum=charNum+1
                if charNum>=len(binMessage):
                   return image
                if (b % 2 == 1) and (binMessage[charNum]==0):
                    b=b-1
                    print(charNum)
                elif (b % 2 == 0) and (binMessage[charNum]==1):
                    b=b+1
                    print(charNum)
                charNum=charNum+1
                if charNum>=len(binMessage):
                   return image
                image.putpixel((i,j),(r,g,b))
			
        return image
        
root = tkinter.Tk()            
ui = userInterfaze(root)
root.mainloop()
