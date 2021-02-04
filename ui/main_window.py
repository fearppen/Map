from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

from app_service.get_map_uc import GetMapUseCase
from domain.map_params import MapParams


class Window(QMainWindow):
    def __init__(self, use_case: GetMapUseCase, parent=None):
        self.use_case = use_case
        self.map_params = MapParams()

        super(QMainWindow, self).__init__(parent)

        uic.loadUi(r"ui\main_window.ui", self)

        self.show_map()

    def keyPressEvent(self, key_event: QtGui.QKeyEvent) -> None:
        key = key_event.key()
        if key == Qt.Key_PageUp:
            self.map_params.zoom_up()
        elif key == Qt.Key_PageDown:
            self.map_params.zoom_down()
        if key == Qt.Key_Left:
            self.map_params.left()
        elif key == Qt.Key_Right:
            self.map_params.right()
        if key == Qt.Key_Up:
            self.map_params.up()
        elif key == Qt.Key_Down:
            self.map_params.down()

        self.show_map()

    def show_map(self):
        map = self.use_case.execute(self.map_params)

        pixmap = QPixmap()
        pixmap.loadFromData(map, "PNG")
        self.map_label.setPixmap(pixmap)
