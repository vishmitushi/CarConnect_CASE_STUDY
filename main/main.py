from dao.AdminService import AdminService
from dao.CustomerService import CustomerService
from dao.ReservationService import ReservationService
from dao.VehicleService import VehicleService



loop = True
table_creation = True
try:
    while loop:
        customerservice1 = CustomerService()
        vehicleservice1 = VehicleService()
        reservationservice1 = ReservationService()
        adminservice1 = AdminService()
        
        while table_creation:
            customerservice1.create_class()
            vehicleservice1.create_class()
            reservationservice1.create_table()
            adminservice1.create_class()
            table_creation= False

        print("Enter your choice: ")
        print("1.Customer management ")
        print("2. Vehicle management ")
        print("3. Reservation")
        print("4. Admin Management")
        print("5. Key Functionalities")
        print("6. Exit")
        choice = int(input("enter your choice:"))

        if choice == 1:
            while True:
                print("1.Add Customer")
                print("2.Update Customer")
                print("3.Delete Customer")
                print("4.Get Customer Details by ID")
                print("5.Get Customer Details by Name")
                print("6.View All Customers")
                print("7.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    customerservice1.RegisterCustomer()
                elif choice == 2:
                    customerservice1.UpdateCustomer()
                elif choice == 3:
                    customerservice1.DeleteCustomer()
                elif choice == 4:
                    customerservice1.GetCustomerById()
                elif choice == 5:
                    customerservice1.GetCustomerByUsername()
                elif choice == 6:
                    customerservice1.select()
                else:
                    break

        elif choice == 2:
            while True:
                print("1.Add Vehicle\t2.Update Vehicle\t3.Remove Vehicle\n4.Get Vehicle Details by ID\t5.View All "
                      "Vehicle\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    vehicleservice1.AddVehicle()
                elif choice == 2:
                    vehicleservice1.UpdateVehicle()
                elif choice == 3:
                    vehicleservice1.RemoveVehicle()
                elif choice == 4:
                    vehicleservice1.GetVehicleById()
                elif choice == 5:
                    vehicleservice1.GetAvailableVehicles()
                else:
                    break

        elif choice == 3:
            while True:
                print("1.Add Reservation\t2.Update Reservation\t3.Delete Reservation\n4.Get Reservation Details by "
                      "ID\t5.Get Reservation Details bu customer ID\t6.Get all reservations\n7.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    reservationservice1.CreateReservation()
                elif choice == 2:
                    reservationservice1.UpdateReservation()
                elif choice == 3:
                    reservationservice1.CancelReservation()
                elif choice == 4:
                    reservationservice1.GetReservationById()
                elif choice == 5:
                    reservationservice1.GetReservationsByCustomerId()
                elif choice == 6:
                    reservationservice1.select()
                else:
                    break

        elif choice == 4:
            while True:
                print("1.Add Admin\t2.Update Admin\t3.Delete Admin\n4.Get Admin Details by "
                      "ID\t5.Get Admin Details bu username\t6.View Admins \n7.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    adminservice1.RegisterAdmin()
                elif choice == 2:
                    adminservice1.UpdateAdmin()
                elif choice == 3:
                    adminservice1.DeleteAdmin()
                elif choice == 4:
                    adminservice1.GetAdminById()
                elif choice == 5:
                    adminservice1.GetAdminByUsername()
                elif choice == 6:
                    adminservice1.select()
                else:
                    break

        elif choice == 5:
            while True:
                print("1.Customer Login\n2.Admin Login\n3.Exit")
                choice = int(input("enter ur number"))
                if choice ==1:
                    customerservice1.authenticate_customer()
                elif choice == 2:
                    adminservice1.authenticate_password()
                else:
                    break
        else:
            loop = False
except Exception as e:
    print(e)





