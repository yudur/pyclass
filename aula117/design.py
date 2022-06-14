# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.btnRedimensionar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRedimensionar.setObjectName("btnRedimensionar")
        self.gridLayout.addWidget(self.btnRedimensionar, 2, 4, 1, 1)
        self.inputLargura = QtWidgets.QLineEdit(self.centralwidget)
        self.inputLargura.setObjectName("inputLargura")
        self.gridLayout.addWidget(self.inputLargura, 2, 1, 1, 1)
        self.inputAltura = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAltura.setObjectName("inputAltura")
        self.gridLayout.addWidget(self.inputAltura, 2, 3, 1, 1)
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setObjectName("btnSalvar")
        self.gridLayout.addWidget(self.btnSalvar, 3, 4, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 491, 310))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelImg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")
        self.gridLayout_2.addWidget(self.labelImg, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)
        self.btnEscolherArquivo = QtWidgets.QPushButton(self.centralwidget)
        self.btnEscolherArquivo.setObjectName("btnEscolherArquivo")
        self.gridLayout.addWidget(self.btnEscolherArquivo, 1, 4, 1, 1)
        self.inputAbrirArquivo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAbrirArquivo.setObjectName("inputAbrirArquivo")
        self.gridLayout.addWidget(self.inputAbrirArquivo, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redimensionar Imagem"))
        self.label.setText(_translate("MainWindow", "Largura"))
        self.label_2.setText(_translate("MainWindow", "Altura"))
        self.btnRedimensionar.setText(_translate("MainWindow", "Redimensionar"))
        self.btnSalvar.setText(_translate("MainWindow", "Salvar"))
        self.btnEscolherArquivo.setText(_translate("MainWindow", "Escolher Arquivo"))
