from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

from app_service.get_coords import GetCoords
from app_service.get_map_uc import GetMapUseCase
from domain.map_params import MapParams
from services.geocoder_adapter import GeocoderAdapter


class Window(QMainWindow):
    def __init__(self, use_case: GetMapUseCase, get_coords: GetCoords, parent=None):
        self.use_case = use_case
        self.map_params = MapParams()
        self.get_coords = get_coords
        self.geocoder_adapter = GeocoderAdapter()

        super(QMainWindow, self).__init__(parent)

        uic.loadUi(r"ui\main_window.ui", self)
        self.pushButton.clicked.connect(self.press_key_button)
        self.comboBox.activated[str].connect(self.changed_combo_box)
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

    def press_key_button(self):
        if self.lineEdit.text():
            coords = self.get_coords.execute(self.geocoder_adapter.get_coords(self.lineEdit.text()))
            self.map_params.set_latitude(coords[1])
            self.map_params.set_longitude(coords[0])
        self.show_map()

    def changed_combo_box(self, text):
        if text == 'Схема':
            self.map_params.change_type_map()
        elif text == 'Спутник':
            self.map_params.change_type_sat()
        elif text == 'Гибрид':
            self.map_params.change_type_sat_skl()

    def show_map(self):
        map = self.use_case.execute(self.map_params)

        pixmap = QPixmap()
        type_map = str()

        if self.map_params.get_type_map() == 'sat' or self.map_params.get_type_map() == 'sat,skl':
            type_map = 'JPG'
        elif self.map_params.get_type_map() == 'map':
            type_map = 'PNG'

        pixmap.loadFromData(map, type_map)
        self.map_label.setPixmap(pixmap)
