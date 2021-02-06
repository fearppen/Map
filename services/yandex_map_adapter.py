import requests

from services.i_map_service import IMapService


class YandexMapAdapter(IMapService):
    map_request = "http://static-maps.yandex.ru/1.x/"

    def get_map(self, longitude: float, latitude: float, zoom: int, type_map: str):
        params = {"pt": f"{longitude},{latitude},vkbkm",
                  "z": zoom,
                  "l": type_map,
                  "size": "650,450"}

        return requests.get(self.map_request, params=params).content
