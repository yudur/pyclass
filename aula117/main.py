from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from design import *
import sys


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_img)
        self.btnRedimensionar.clicked.connect(self.redimencionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_img(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            "abrir imagem",
            r"/Users/user/Pictures"
        )
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimencionar(self):
        largura = int(self.inputLargura.text())
        self.nova_img = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_img)
        self.inputLargura.setText(str(self.nova_img.width()))
        self.inputAltura.setText(str(self.nova_img.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            "salvar imagem",
            r"/Users/user/Desktop"
        )
        self.nova_img.save(imagem, 'png')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
