from services.i_find_coords_service import IFindCoordsService


class GetCoords:
    def __init__(self, service: IFindCoordsService):
        self.service = service

    def execute(self, param):
        return tuple(map(float, param['response']['GeoObjectCollection']['featureMember']
                         [0]['GeoObject']['Point']['pos'].split()))
