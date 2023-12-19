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















 # Test adding a new vehicle.
    # def test3(self):
    #     print("add vehicle details")
    #     result = self.vehicleservice1.AddVehicle()
    #     self.assertEqual('Vehicle added successfully', result)
    # # Test updating vehicle details.
    # def test4(self):
    #     print(" enter vehicle details to update. Select customerID = 4")
    #     result = self.vehicleservice1.UpdateVehicle()
    #     self.assertEqual(True, result)
    # # Test getting a list of available vehicles.
    # def test5(self):
    #     print("getting list of available vehicles")
    #     result = self.vehicleservice1.CountofVehicles()
    #     self.assertEqual(result[0][0],len( self.vehicleservice1.GetAvailableVehicles()))
    # # Test getting a list of all vehicles.
    # def test6(self):
    #     print("checking whether table is created or not")
    #     result = self.reservationservice1.create_table()
    #     self.assertEqual(result, True )

