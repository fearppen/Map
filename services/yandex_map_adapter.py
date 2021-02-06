import requests

from services.i_map_service import IMapService


class YandexMapAdapter(IMapService):
    map_request = "http://static-maps.yandex.ru/1.x/"

    def get_map(self, longitude, latitude, zoom, type_map):
        return requests.get(self.map_request, params={"pt": f"{longitude},{latitude}",
                                                      "z": zoom,
                                                      "l": type_map}).content
