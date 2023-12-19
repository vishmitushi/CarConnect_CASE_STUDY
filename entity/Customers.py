from datetime import datetime


class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address, username, password):
        self.CustomerID = customer_id
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.PhoneNumber = phone_number
        self.Address = address
        self.Username = username
        self.Password = password
        self.RegistrationDate = datetime.now()

    def Authenticate(self):
        pass


customer1 = Customer(1, "aditya", "nagavolu", "adi@gmail.com", "982753", "Hills State", "messi", "uihemacj")
