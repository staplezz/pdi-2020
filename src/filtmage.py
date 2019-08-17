import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton,
 QAction, QFileDialog, QLabel, QSizePolicy, QComboBox, QSlider, QVBoxLayout,
 QLineEdit, QFrame)
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageQt
import filtroBlancoyNegro
import filtroColores
import filtroAltoContraste

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Filtmage'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 440
        self.initUI()
        self.nombreArch = None
        
        
    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Menu bar.
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Archivo')
        abrir = QAction('Abrir', self)
        fileMenu.addAction(abrir)
        abrir.setShortcut('Ctrl+O')

        #Para abrir archivo
        abrir.triggered.connect(self.openFileNameDialog)

        #Para mostrar la imágen.
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(60, 100, 281, 271))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setText("Abre una imágen para aplicar un filtro")
        self.imageLabel.setFrameShape(QFrame.StyledPanel)

        #Imágen con el filtro aplicado.
        self.imageFiltro = QtWidgets.QLabel(self.centralwidget)
        self.imageFiltro.setGeometry(QtCore.QRect(450, 100, 281, 271))
        self.imageFiltro.setScaledContents(True)
        self.imageFiltro.setFrameShape(QFrame.StyledPanel)

        #Combo box para los filtros.
        self.comboBox = QComboBox(self)
        self.comboBox.move(60,50)
        self.comboBox.addItems(["Blanco Y Negro", "Rojo", "Verde", "Azul",
            "Mosaico", "Alto Contraste", "Inverso", "Brillo"])

        #Botón aplica filtro.
        self.aplicaFiltro = QPushButton("Aplica filtro", self)
        self.aplicaFiltro.move(240, 50)
        self.aplicaFiltro.clicked.connect(self.filtro)

        #Slider para algunos filtros
        vBoxLayout = QVBoxLayout()
        self.lineEdit = QLineEdit(self)
        vBoxLayout.addWidget(self.lineEdit)
        self.lineEdit.move(620, 50)

        self.sliderFiltro = QSlider(Qt.Horizontal, self)
        self.sliderFiltro.move(450, 50)
        self.sliderFiltro.setMinimum(-127)
        self.sliderFiltro.setMaximum(127)
        self.sliderFiltro.setValue(0)
        self.sliderFiltro.valueChanged.connect(self.changedValue)
        vBoxLayout.addWidget(self.sliderFiltro)

        self.setCentralWidget(self.centralwidget)
        self.show()

    #Aplica el filtro seleccionado a la imágen.
    def filtro(self):
        filtro = self.comboBox.currentText()
        valor = int(self.sliderFiltro.value())
        #Seleccionamos el filtro adecuado.
        if (filtro == "Blanco Y Negro"):
            imagen = filtroBlancoYNegro.blancoYNegro(self.nombreArch)
        if (filtro == "Rojo"):
            imagen = filtroColores.filtroRojo(self.nombreArch)
        if (filtro == "Verde"):
            imagen = filtroColores.filtroVerde(self.nombreArch)
        if (filtro == "Azul"):
            imagen = filtroColores.filtroAzul(self.nombreArch)
        if (filtro == "Alto Contraste"):
            imagen = filtroAltoContraste.altoContraste(self.nombreArch)
        if (filtro == "Inverso"):
            imagen = filtroAltoContraste.inverso(self.nombreArch)
        if (filtro == "Mosaico"):
            imagen = filtroAltoContraste.mosaico(self.nombreArch, valor)
        if (filtro == "Brillo"):
            imagen = filtroAltoContraste.brillo(self.nombreArch, valor)

        imagen = imagen.convert("RGBA")
        data = imagen.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, imagen.size[0], imagen.size[1], QtGui.QImage.Format_ARGB32)
        pix = QtGui.QPixmap.fromImage(qim)
        self.imageFiltro.setPixmap(pix)
        #filtro = self.comboBox.currentText()


    #File Dialog para abrir un archivo de imágen.
    def openFileNameDialog(self):
        fileName = QFileDialog.getOpenFileName(self, "Abrir Imágen", '/home',
        "Image (*.jpg *.png *jpeg);;Todos los archivos (*)")
        self.nombreArch = fileName[0]
        self.image = QImage(fileName[0])
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
        self.scaleFactor = 1.0

    #Cambia el valor del VBox para mostar.
    def changedValue(self):
        size = str(self.sliderFiltro.value())
        self.lineEdit.setText(size)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
