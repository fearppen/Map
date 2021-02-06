from services.i_obj_service import IObjService


class GetAddress:
    def __init__(self, service: IObjService):
        self.service = service

    def execute(self, param):
        return param["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"] \
               ["metaDataProperty"]["GeocoderMetaData"]["text"]
