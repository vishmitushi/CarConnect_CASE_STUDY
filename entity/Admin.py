class Admin:
    def __init__(self, admin_id, first_name, last_name, email, phone_number, username, password, role, join_date):
        self.AdminID = admin_id
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.PhoneNumber = phone_number
        self.Username = username
        self.Password = password
        self.Role = role
        self.JoinDate = join_date

    def Authenticate(self, entered_password):
        pass


# Example usage:
admin1 = Admin(1, "John", "Doe", "john.doe@example.com", "123-456-7890", "john_doe", "admin_password", "Admin", "2023-01-01")
