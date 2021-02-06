import requests

from services.i_find_coords_service import IFindCoordsService


class GeocoderAdapter(IFindCoordsService):
    map_request = "http://geocode-maps.yandex.ru/1.x/"

    def get_coords(self, name):
        return requests.get(self.map_request,
                            params={"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                                    "geocode": name,
                                    "format": "json"}).json()
