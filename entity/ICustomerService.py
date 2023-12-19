from abc import ABC, abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def GetCustomerById(self):
        pass

    @abstractmethod
    def GetCustomerByUsername(self):
        pass

    @abstractmethod
    def RegisterCustomer(self):
        pass

    @abstractmethod
    def UpdateCustomer(self):
        pass

    @abstractmethod
    def DeleteCustomer(self):
        pass
