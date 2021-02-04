from services.i_map_service import IMapService


class GetMapUseCase:
    def __init__(self, map_service: IMapService):
        self.map_service = map_service

    def execute(self, param: dict):
        return self.map_service.get_map(param["longitude"], param["latitude"], param["zoom"])
