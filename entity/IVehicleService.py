from abc import ABC, abstractmethod


class IVehicleService(ABC):
    @abstractmethod
    def GetVehicleById(self):
        pass

    @abstractmethod
    def GetAvailableVehicles(self):
        pass

    @abstractmethod
    def AddVehicle(self):
        pass

    @abstractmethod
    def UpdateVehicle(self):
        pass

    @abstractmethod
    def RemoveVehicle(self):
        pass
