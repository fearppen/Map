from services.i_find_coords_service import IFindCoordsService


class GetAddress:
    def __init__(self, service: IFindCoordsService):
        self.service = service

    def execute(self, param):
        return param["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"] \
               ["metaDataProperty"]["GeocoderMetaData"]["text"]
