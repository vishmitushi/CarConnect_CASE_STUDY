from abc import ABC, abstractmethod


class IAdminService(ABC):
    @abstractmethod
    def GetAdminById(self):
        pass

    @abstractmethod
    def GetAdminByUsername(self):
        pass

    @abstractmethod
    def RegisterAdmin(self):
        pass

    @abstractmethod
    def UpdateAdmin(self):
        pass

    @abstractmethod
    def DeleteAdmin(self):
        pass
