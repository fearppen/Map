import requests

from services.i_obj_service import IObjService


class GeocoderAdapter(IObjService):
    map_request = "http://geocode-maps.yandex.ru/1.x/"

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

    def get_organization(self, longitude, latitude):
        return requests.get(self.map_request,
                            params={"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                                    "geocode": f"{longitude},{latitude}",
                                    "ll": f"{longitude},{latitude}",
                                    "spn": f"{0.0009009},{0.0009009}",
                                    "format": "json"}).json()
