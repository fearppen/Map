import requests
from domain.map_params import MapParams
from services.i_obj_service import IObjService


class GeocoderAdapter(IObjService):
    map_request = "http://geocode-maps.yandex.ru/1.x/"

    def __init__(self):
        self.map_params = MapParams()

    def get_coords(self, name):
        return requests.get(self.map_request,
                            params={"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                                    "geocode": name,
                                    "format": "json"}).json()

    def get_object(self, longitude, latitude):
        return requests.get(self.map_request,
                            params={"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                                    "geocode": f"{longitude},{latitude}",
                                    "format": "json"}).json()
