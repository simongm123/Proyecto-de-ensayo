from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi
import sys
import numpy as np
#hola mundo

class Ventana_Principal(QWidget):
    def __init__(self):
        super(Ventana_Principal,self).__init__()
        loadUi('Ejemplo.ui',self)
        self.cont=0;
        self.IngresarBot.clicked.connect(self.Oprimido)
        self.IngNombre.cursorPositionChanged.connect(self.Cursorcito)
        
    def Oprimido(self):
        self._tiempo=np.arange(0,50)
        self._sin=np.sin(self._tiempo)
        self.ploteador.plot(self._sin,self._tiempo)
        
        nombre=self.IngNombre.text()
        print(nombre)
        self.IngNombre.setText('')
        
    def Cursorcito(self):
        self.cont=self.cont+1
        print(self.cont)


app=QApplication(sys.argv)
ventana=Ventana_Principal()
ventana.show()

sys.exit(app.exec_())