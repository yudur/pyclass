import sys
from calc_cpf import valida_cpf
from gera_cpf import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import design


class GeraValidaCPF(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCPF.clicked.connect(self.gera_cpf)
        self.btnValidaCPF.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        cpf = gera_cpf()
        self.laberRetorno.setText(f"{cpf} - Valido")

    def valida_cpf(self):
        cpf = self.inputValidaCPF.text()

        if valida_cpf(cpf):
            self.laberRetorno.setText(f"{cpf} - Valido")
        elif not cpf:
            self.laberRetorno.setText("Invalido")
        else:
            self.laberRetorno.setText(f"{cpf} - Invalido")


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    gera_valida_CPF = GeraValidaCPF()
    gera_valida_CPF.show()
    qt.exec_()
