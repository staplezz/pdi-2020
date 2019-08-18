from PIL import Image
import os

'''
Filtro rojo:
Obtenemos el valor del canal rojo y simplemente
lo vamos agregando a cada pixel hasta terminar la
imágen.
'''
def filtroRojo(imagen):
	imagen = Image.open(imagen)
	datas = imagen.getdata()
	width, height = imagen.size
	pixelesNuevos = []

	for item in datas:
		redValue = item[2]
		pixelesNuevos.append((0, 0, redValue))

	imagen.putdata(pixelesNuevos)
	return imagen

'''
Filtro verde:
Obtenemos el valor del canal verde y simplemente
lo vamos agregando a cada pixel hasta terminar la
imágen.
'''
def filtroVerde(imagen):
	imagen = Image.open(imagen)
	datas = imagen.getdata()
	width, height = imagen.size
	pixelesNuevos = []

	for item in datas:
		greenValue = item[1]
		pixelesNuevos.append((0, greenValue, 0))

	imagen.putdata(pixelesNuevos)
	return imagen

'''
Filtro azul:
Obtenemos el valor del canal azul y simplemente
lo vamos agregando a cada pixel hasta terminar la
imágen.
'''
def filtroAzul(imagen):
	imagen = Image.open(imagen)
	datas = imagen.getdata()
	width, height = imagen.size
	pixelesNuevos = []

	for item in datas:
		blueValue = item[0]
		pixelesNuevos.append((blueValue, 0, 0))

	imagen.putdata(pixelesNuevos)
	return imagen
