from services.i_obj_service import IObjService


class GetCoords:
    def __init__(self, service: IObjService):
        self.service = service

    def execute(self, param):
        return tuple(map(float, param['response']['GeoObjectCollection']['featureMember']
                         [0]['GeoObject']['Point']['pos'].split()))
