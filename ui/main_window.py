from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

from app_service.get_map_uc import GetMapUseCase
from domain.map_params import MapParams


class Window(QMainWindow):
    def __init__(self, use_case: GetMapUseCase, parent=None):
        self.use_case = use_case

        super(QMainWindow, self).__init__(parent)

        uic.loadUi(r"D:\Map\ui\main_window.ui", self)

        self.show_map()

    def show_map(self):
        map_params = MapParams()
        map = self.use_case.execute(map_params)

        pixmap = QPixmap()
        pixmap.loadFromData(map, "PNG")
        self.map_label.setPixmap(pixmap)
