import sys
from ejemplo import *
from PyQt5.QtWidgets import *


class Ventana(QWidget):
    def __init__(self, parent = None):
       QtWidgets.QWidget. __init__(self,parent)
       self.ui = Ui_Form()
       self.ui.setupUi(self)
       self.ui.btnSumar.clicked.connect(self.sumar)
       

    def sumar(self):
        n1=self.ui.txtNumero1.toPlainText()
        n2=self.ui.txtNumero2.toPlainText()
        n1=int(n1)
        n2 = int(n2)
        suma= n1+ n2

        self.ui.lblSalida.setText("La suma es " +str(suma))

    
    
if __name__ == "__main__":
    mi_aplicacion = QApplication(sys.argv)
    mi_app= Ventana()
    mi_app.show()
    sys.exit(mi_aplicacion.exec_())
        
       
            