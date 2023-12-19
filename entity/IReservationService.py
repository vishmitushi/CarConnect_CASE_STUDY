from abc import ABC, abstractmethod

class IReservationService(ABC):
    @abstractmethod
    def GetReservationById(self):
        pass

    @abstractmethod
    def GetReservationsByCustomerId(self):
        pass

    @abstractmethod
    def CreateReservation(self):
        pass

    @abstractmethod
    def UpdateReservation(self):
        pass

    @abstractmethod
    def CancelReservation(self):
        pass
