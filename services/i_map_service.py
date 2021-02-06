from abc import ABC, abstractmethod


class IMapService(ABC):
    @abstractmethod
    def get_map(self, longitude: float, latitude: float, zoom: int, type_map: str):
        pass
