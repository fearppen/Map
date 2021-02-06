from abc import ABC, abstractmethod


class IFindCoordsService(ABC):
    @abstractmethod
    def get_coords(self, name: str):
        pass
