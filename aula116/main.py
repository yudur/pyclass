import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.disply = QLineEdit()
        self.grid.addWidget(self.disply, 0, 0, 1, 5)
        self.disply.setDisabled(True)
        self.disply.setStyleSheet(
            '* {background: #FFF; color: #000; font-size: 30px;}'
        )
        self.disply.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(QPushButton('C'), 1, 4, 1, 1,
                     lambda: self.disply.setText(''),
                     'background: #d5580d; color: #fff; font-weight: 700;'
                     )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(QPushButton('<-'), 2, 4, 1, 1,
                     lambda: self.disply.setText(
                         self.disply.text()[:-1]
                     ),
                     'background: #13823a; color: #fff; font-weight: 700;'
                     )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('*'), 3, 3, 1, 1)
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('/'), 4, 3, 1, 1)
        self.add_btn(QPushButton('='), 4, 4, 1, 1,
                     self.eval_igual,
                     'background: #095177; color: #fff; font-weight: 700;'
                     )

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, func=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not func:
            btn.clicked.connect(
                lambda: self.disply.setText(
                    self.disply.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(func)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.disply.setText(
                str(eval(self.disply.text()))
            )
        except Exception as e:
            self.disply.setText('conta inválida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    qt.exec_()
