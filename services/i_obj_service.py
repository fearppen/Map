from abc import ABC, abstractmethod


class IObjService(ABC):
    @abstractmethod
    def get_coords(self, name: str):
        pass

    def get_object(self, longitude: float, latitude: float):
        pass

    def get_organization(self, longitude: float, latitude: float):
        pass
