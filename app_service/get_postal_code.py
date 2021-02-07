from services.i_obj_service import IObjService


class GetPostalCode:
    def __init__(self, service: IObjService):
        self.service = service

    def execute(self, param):
        return param["response"]["GeoObjectCollection"]["featureMember"][
            0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]

    def execute_by_coords(self, param):
        return param["response"]["GeoObjectCollection"]["featureMember"] \
            [0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
