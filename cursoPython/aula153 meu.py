
'''
pip install pyqt5
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout

class App(QMainWindow):         # herdou QMainWindow
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('Texto do botão')
        self.btn.setStyleSheet('font-size: 40px;')
        # self.btn.clicked.connect(lambda: print('Olá Mundo'))
        self.btn.clicked.connect(self.acao)
        self.grid.addWidget(self.btn, 0, 0, 1, 1)   # x, y, qtd linhas ocupa, qtd colunas ocupa
        self.setCentralWidget(self.cw)

    def acao(self):
        print('Alguma coisa')

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()