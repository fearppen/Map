from abc import ABC, abstractmethod


class IObjService(ABC):
    @abstractmethod
    def get_coords(self, name: str):
        pass

    @abstractmethod
    def get_object(self, longitude: float, latitude: float):
        pass
