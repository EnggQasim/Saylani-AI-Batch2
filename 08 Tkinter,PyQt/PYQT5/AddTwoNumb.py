# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTwoNumb.ui'

# Created by: PyQt5 UI code generator 5.6

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")

        Dialog.resize(400, 300)

        self.label = QtWidgets.QLabel(Dialog)

        self.label.setGeometry(QtCore.QRect(30, 40, 161, 16))

        font = QtGui.QFont()

        font.setPointSize(14)

        self.label.setFont(font)

        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)

        self.label_2.setGeometry(QtCore.QRect(30, 80, 181, 16))

        font = QtGui.QFont()

        font.setPointSize(14)

        self.label_2.setFont(font)

        self.label_2.setObjectName("label_2")

        self.lineEditFirstNumb = QtWidgets.QLineEdit(Dialog)

        self.lineEditFirstNumb.setGeometry(QtCore.QRect(220, 40, 113, 20))

        font = QtGui.QFont()

        font.setPointSize(14)

        self.lineEditFirstNumb.setFont(font)

        self.lineEditFirstNumb.setObjectName("lineEditFirstNumb")

        self.lineEditSecondNumb = QtWidgets.QLineEdit(Dialog)

        self.lineEditSecondNumb.setGeometry(QtCore.QRect(220, 80, 113, 20))

        font = QtGui.QFont()

        font.setPointSize(14)

        self.lineEditSecondNumb.setFont(font)

        self.lineEditSecondNumb.setObjectName("lineEditSecondNumb")

        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)

        self.pushButtonAdd.setGeometry(QtCore.QRect(150, 120, 75, 23))

        font = QtGui.QFont()

        font.setPointSize(14)

        self.pushButtonAdd.setFont(font)

        self.pushButtonAdd.setObjectName("pushButtonAdd")

        self.labelResponse = QtWidgets.QLabel(Dialog)

        self.labelResponse.setGeometry(QtCore.QRect(50, 200, 321, 20))

        font = QtGui.QFont()

        font.setPointSize(14)

        self.labelResponse.setFont(font)

        self.labelResponse.setObjectName("labelResponse")

 

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

 

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate

        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.label.setText(_translate("Dialog", "Enter first number"))

        self.label_2.setText(_translate("Dialog", "Enter second number"))

        self.pushButtonAdd.setText(_translate("Dialog", "Add"))

        self.labelResponse.setText(_translate("Dialog", "TextLabel"))

 

if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)

    Dialog = QtWidgets.QDialog()

    ui = Ui_Dialog()

    ui.setupUi(Dialog)

    Dialog.show()

    sys.exit(app.exec_())
