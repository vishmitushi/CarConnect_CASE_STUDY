import unittest
from dao.CustomerService import CustomerService
from dao.ReservationService import ReservationService
from dao.VehicleService import VehicleService


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.customerservice1 = CustomerService()
        self.vehicleservice1 = VehicleService()
        self.reservationservice1 = ReservationService()

    # #Test customer authentication with invalid credentials.
    def test_customer_credential(self):
        print("enter invalid credentials customerID=1 and password = messi")
        result = self.customerservice1.authenticate_customer()
        self.assertEqual("Incorrect password",str(result))
    # # Test updating customer information.
    def test_customer_info(self):
        print(" enter customer details to update. Select customerID = 4")
        result = self.customerservice1.UpdateCustomer()
        self.assertEqual('Customer Record updated successfully' , result)

if __name__ == '__main__':
    unittest.main()















 
