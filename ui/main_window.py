import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)

        uic.loadUi("main_window.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
