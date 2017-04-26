# -*- encoding: utf-8 -*-
import binascii

def lessBit(image,fText):
	width,height = image.size
	maxLetters = width*height*3
	message = fText.read()
	binMessage = binascii.a2b_uu(message)
	if maxLetters < message.length:
		return 0
		
	for i in range(width):
		for j in range(height):
			r,g,b = image.getpixel((i,j))
			
	return newImage
