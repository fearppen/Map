from services.i_obj_service import IObjService


class GetAddress:
    def __init__(self, service: IObjService):
        self.service = service

    def execute(self, param):
        return param["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"] \
               ["metaDataProperty"]["GeocoderMetaData"]["text"]

    def execute_organization(self, param):
        all_names = param["response"]["GeoObjectCollection"]["featureMember"]
        for i in all_names:
            if i['GeoObject']['metaDataProperty']['GeocoderMetaData']['kind'] == 'house':
                return i['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
