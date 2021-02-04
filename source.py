import sys

from PyQt5.QtWidgets import QApplication

from app_service.get_map_uc import GetMapUseCase
from services.yandex_map_adapter import YandexMapAdapter
from ui.main_window import Window

if __name__ == '__main__':
    adapter = YandexMapAdapter()
    use_case = GetMapUseCase(adapter)
    app = QApplication(sys.argv)
    main = Window(use_case)
    main.show()
    sys.exit(app.exec_())
