# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejemplo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1104, 702)
        self.btnSumar = QtWidgets.QPushButton(Form)
        self.btnSumar.setGeometry(QtCore.QRect(500, 340, 211, 71))
        self.btnSumar.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.btnSumar.setObjectName("btnSumar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 70, 331, 111))
        self.label.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 170, 331, 111))
        self.label_2.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.txtNumero1 = QtWidgets.QTextEdit(Form)
        self.txtNumero1.setGeometry(QtCore.QRect(510, 100, 141, 61))
        self.txtNumero1.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.txtNumero1.setObjectName("txtNumero1")
        self.txtNumero2 = QtWidgets.QTextEdit(Form)
        self.txtNumero2.setGeometry(QtCore.QRect(510, 180, 141, 61))
        self.txtNumero2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.txtNumero2.setObjectName("txtNumero2")
        self.lblSalida = QtWidgets.QLabel(Form)
        self.lblSalida.setGeometry(QtCore.QRect(130, 290, 331, 91))
        self.lblSalida.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.lblSalida.setObjectName("lblSalida")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnSumar.setText(_translate("Form", "Sumar"))
        self.label.setText(_translate("Form", "Ingrese un entero:"))
        self.label_2.setText(_translate("Form", "Ingrese otro entero:"))
        self.lblSalida.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Salida</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
