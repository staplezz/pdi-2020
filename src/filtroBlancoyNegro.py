from PIL import Image, ImageQt
import os

'''
Filtro escala de grises:
Usamos la fórmula de escala de grises para obtener las
proporciones adecuadas para cada canal y luego las asignamos a
cada pixel dependiendo del cálculo.
'''
def blancoYNegro(imagen):
	imagen = Image.open(imagen)
	datas = imagen.getdata()
	width, height = imagen.size
	pixelesByN = []

	for item in datas:
		redValue = item[0]
		greenValue = item[1]
		blueValue = item[2]
		grayValue = int(.299*redValue + .587*greenValue + .114*blueValue)
		pixelesByN.append((grayValue,grayValue,grayValue))

	imagen.putdata(pixelesByN)

	return imagen
	
