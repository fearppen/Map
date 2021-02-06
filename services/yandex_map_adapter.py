import requests

from services.i_map_service import IMapService


class YandexMapAdapter(IMapService):
    map_request = "http://static-maps.yandex.ru/1.x/"

    def get_map(self, start_longitude, start_latitude, longitude, latitude, zoom, type_map):
        return requests.get(self.map_request, params={"ll": f"{longitude},{latitude}",
                                                      "pt": f"{start_longitude},"
                                                            f"{start_latitude},vkbkm",
                                                      "z": zoom,
                                                      "l": type_map}).content
