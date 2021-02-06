import sys

from PyQt5.QtWidgets import QApplication

from app_service.get_address import GetAddress
from app_service.get_map_uc import GetMapUseCase
from services.yandex_map_adapter import YandexMapAdapter
from ui.main_window import Window
from services.geocoder_adapter import GeocoderAdapter
from app_service.get_coords import GetCoords


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    yandex_adapter = YandexMapAdapter()
    use_case = GetMapUseCase(yandex_adapter)
    geocoder_adapter = GeocoderAdapter()
    get_coords = GetCoords(geocoder_adapter)
    get_address = GetAddress(geocoder_adapter)
    app = QApplication(sys.argv)
    main = Window(use_case, get_coords, get_address)
    main.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
