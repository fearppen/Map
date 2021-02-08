from services.i_organiztion_service import IOrgService
import requests
import math


class ObjectServiceAdapter(IOrgService):
    map_request = 'https://search-maps.yandex.ru/v1/'

    def get_organization(self, longitude, latitude, name_org):
        return requests.get(self.map_request,
                            params={"apikey": "f85da96a-151f-44a3-8f24-6d1843d82922",
                                    "text": f"{name_org}",
                                    "type": "biz",
                                    "ll": f"{longitude},{latitude}",
                                    "spn": f"{0.00045045},"
                                           f"{0.00045045 / 2 * math.cos(math.radians(latitude))}",
                                    'lang': "ru_RU"}).json()

