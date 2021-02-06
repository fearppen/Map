import requests

from services.i_map_service import IMapService


class YandexMapAdapter(IMapService):
    map_request = "http://static-maps.yandex.ru/1.x/"

<<<<<<< HEAD
    def get_map(self, start_longitude, start_latitude, longitude, latitude, zoom, type_map):
        return requests.get(self.map_request, params={"ll": f"{longitude},{latitude}",
                                                      "pt": f"{start_longitude},"
                                                            f"{start_latitude},vkbkm",
                                                      "z": zoom,
                                                      "l": type_map}).content
=======
    def get_map(self, longitude: float, latitude: float, zoom: int, type_map: str):
        params = {"pt": f"{longitude},{latitude},vkbkm",
                  "z": zoom,
                  "l": type_map,
                  "size": "650,450"}

        return requests.get(self.map_request, params=params).content
>>>>>>> c2cd47234b47bbd380e09042246c0bd0b2b92eeb
