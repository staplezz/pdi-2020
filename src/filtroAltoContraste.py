from PIL import Image
import os

#Filtro de Alto Contraste.
def altoContraste(imagen):
	imagen = Image.open(imagen)
	datas = imagen.getdata()
	width, height = imagen.size
	pixelesNuevos = []

	for item in datas:
		redValue = item[0]
		greenValue = item[1]
		blueValue = item[2]

		if(((redValue + greenValue + blueValue) / 3) > 127):
			pixelesNuevos.append((255, 255, 255))
		else:
			pixelesNuevos.append((0, 0, 0))

	imagen.putdata(pixelesNuevos)

	return imagen

#Filtro de Inverso.
def inverso(imagen):
	imagen = Image.open(imagen)
	datas = imagen.getdata()
	width, height = imagen.size
	pixelesNuevos = []

	for item in datas:
		redValue = item[0]
		greenValue = item[1]
		blueValue = item[2]

		if(((redValue + greenValue + blueValue) / 3) < 127):
			pixelesNuevos.append((255, 255, 255))
		else:
			pixelesNuevos.append((0, 0, 0))

	imagen.putdata(pixelesNuevos)

	return imagen

#Filtro Mosaico
def mosaico(imagen, numeroDeMosaicos):
	imagen = Image.open(imagen)
	datas = imagen.getdata()

	if(numeroDeMosaicos <= 0):
		pixelesNuevos = []
		for pixel in datas:
			redValue = pixel[2]
			greenValue = pixel[1]
			blueValue = pixel[0]
			pixelesNuevos.append((redValue, greenValue, blueValue))
		imagen.putdata(pixelesNuevos)
		return imagen

	width, height = imagen.size

	x = y = redValue = greenValue = blueValue = m = n = 0

	while(x < width):
		if ((x + numeroDeMosaicos) < width):
			m = numeroDeMosaicos
		else:
			m = width - x

		while(y < height):
			if ((y + numeroDeMosaicos) < height):
				n = numeroDeMosaicos
			else:
				n = height - y

			for i in range(m):
				for j in range(n):
					colorC = imagen.getpixel((i + x, j + y))
					blueValue += colorC[0]
					greenValue += colorC[1]
					redValue += colorC[2]

			redValue = int(redValue / (m * n));
			greenValue = int(greenValue / (m * n));
			blueValue = int(blueValue / (m * n));

			for i in range(m):
				for j in range(n):
					imagen.putpixel((i + x, j + y), 
					(redValue, greenValue, blueValue))
			y += n 
			redValue = 0;
			greenValue = 0; 
			blueValue = 0;

		x += m
		y = 0;

	return imagen

#Filtro de brillo.
def brillo(imagen, factor):
	imagen = Image.open(imagen)
	width, height = imagen.size
	datas = imagen.getdata()
	pixelesNuevos = []

	for pixel in datas:
		redValue = pixel[2] + factor
		greenValue = pixel[1] + factor
		blueValue = pixel[0] + factor
		
		#Vemos que no se pase de 255 o que sea menos de 0.
		redValue = min(max(redValue,0),255)
		greenValue = min(max(greenValue,0),255)
		blueValue = min(max(blueValue,0),255)

		pixelesNuevos.append((redValue, greenValue, blueValue))

	imagen.putdata(pixelesNuevos)

	return imagen
