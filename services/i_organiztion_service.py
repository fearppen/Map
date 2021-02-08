from abc import ABC, abstractmethod


class IOrgService(ABC):
    @abstractmethod
    def get_organization(self, longitude: float, latitude: float, name_org: str):
        pass
