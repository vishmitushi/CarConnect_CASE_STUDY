from entity.ICustomerService import ICustomerService
from exception.AuthenticationException import AuthenticationException
from exception.CustomException import CustomException, StringCheck, validate_email, validate_phone
from util.DBConnUtil import dbConnection
import hashlib


def custom_hash_password(password1):
    salt = "$2a$10$[}0w3rima-=-723%.;/'!87&*||]\]"
    password = password1
    combined_string = password + salt
    sha256 = hashlib.sha256()
    sha256.update(combined_string.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password


class CustomerService(dbConnection ,ICustomerService):

    def create_class(self):
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS Customer (
                CustomerID INT PRIMARY KEY AUTO_INCREMENT,
                FirstName VARCHAR(40),
                LastName VARCHAR(40),
                Email VARCHAR(40),
                PhoneNumber CHAR(12),
                Address VARCHAR(100),
                Username VARCHAR(55) UNIQUE,
                Password VARCHAR(255),
                RegistrationDate DATE
            );
            """
            self.open()
            self.stmt.execute(create_table_query)
            self.conn.commit()
            print("--Table 'Customer' created successfully:--")
            self.close()
        except Exception as e:
            print(str(e) + "---Error creating table 'Customer':--")

    def RegisterCustomer(self):
        try:
            first_name = input("Enter First Name: ")
            if not isinstance(first_name, str):
                raise CustomException("Enter string only")
            StringCheck(first_name)
            self.first_name = first_name

            last_name = input("Enter Last Name: ")
            if not isinstance(last_name, str):
                raise CustomException("Enter string only")
            StringCheck(last_name)
            self.last_name = last_name

            email = input("Enter Email: ")
            if not isinstance(email, str):
                raise CustomException("Enter string only")
            validate_email(email)
            self.email = email

            phone_number = input("Enter Phone Number: ")
            if not isinstance(phone_number, str):
                raise CustomException("Enter string only")
            validate_phone(phone_number)
            self.phone_number = phone_number

            address = input("Enter Address: ")
            if not isinstance(address, str):
                raise CustomException("Enter string only")
            self.address = address

            username = input("Enter Username: ")
            if not isinstance(username, str):
                raise CustomException("Enter string only")
            StringCheck(username)
            self.username = username

            password = input("Enter Password: ")
            self.password = custom_hash_password(password)

            registration_date = input("Enter Registration Date (YYYY-MM-DD): ")
            self.registration_date = registration_date

            insert_query = """
            INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
            self.open()
            self.stmt.execute(
                insert_query,
                (
                    self.first_name,
                    self.last_name,
                    self.email,
                    self.phone_number,
                    self.address,
                    self.username,
                    self.password,
                    self.registration_date,
                ),
            )
            self.conn.commit()
            print("--Customer added successfully:--")
            self.close()

        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error adding customer:--")

    def select(self):
        try:
            select_query = """SELECT * FROM Customer;"""
            self.open()
            self.stmt.execute(select_query)
            data = self.stmt.fetchall()
            if data:
                print("-- Customer Data --")
                for row in data:
                    print(f"CustomerID: {row[0]},\n FirstName: {row[1]},\n LastName: {row[2]}, \nEmail: {row[3]}, "
                          f"\nPhoneNumber: {row[4]},\n Address: {row[5]},\n Username: {row[6]},\n Password: {row[7]}, "
                          f"\nRegistrationDate: {row[8]}")
                self.close()
            else:
                raise CustomException("-- No customers found in the database --")

        except Exception as e:
            print(str(e) + "---Error selecting data from 'Customer':--")

    def UpdateCustomer(self):
        try:
            self.select()
            customer_id = int(input('Enter Customer ID to be Updated: '))
            if customer_id < 0:
                raise CustomException("ID should be positive")
            update_customer_str = 'UPDATE Customer SET '
            data = []

            self.email = input('Enter Email (Press Enter to skip): ')
            if self.email:
                validate_email(self.email)
                update_customer_str += 'Email=%s, '
                validate_email(self.email)
                data.append(self.email)

            self.phone_number = input('Enter Phone Number (Press Enter to skip): ')
            if self.phone_number:
                validate_phone(self.phone_number)
                update_customer_str += 'PhoneNumber=%s, '
                validate_phone(self.phone_number)
                data.append(self.phone_number)

            self.address = input('Enter Address (Press Enter to skip): ')
            if self.address:
                update_customer_str += 'Address=%s, '
                data.append(self.address)

            self.username = input('Enter Username (Press Enter to skip): ')
            if self.username:
                update_customer_str += 'Username=%s, '
                data.append(self.username)

            self.password = input('Enter Password (Press Enter to skip): ')
            if self.password:
                self.password = custom_hash_password(self.password)
                update_customer_str += 'Password=%s, '
                data.append(self.password)
                print(data)

            update_customer_str = update_customer_str.rstrip(', ')

            update_customer_str += ' WHERE CustomerID=%s'
            data.append(customer_id)
            self.open()
            self.stmt.execute(update_customer_str, data)
            self.conn.commit()
            print('Customer Record updated successfully.')
            return f'Customer Record updated successfully'
        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + '---Error updating customer details:--')

    def DeleteCustomer(self):
        try:
            customer_id = int(input("Enter Customer ID to be deleted: "))
            if not isinstance(customer_id, int) or customer_id < 0:
                raise CustomException("Enter a positive integer for Customer ID only")

            delete_query = "DELETE FROM Customer WHERE CustomerID = %s"

            self.open()
            self.stmt.execute(delete_query, (customer_id,))
            self.conn.commit()
            print(f"Customer with ID {customer_id} deleted successfully.")
            self.close()

        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error deleting customer:--")

    def GetCustomerById(self):
        try:
            customer_id = int(input("enter ID :"))
            query = "SELECT * FROM Customer WHERE CustomerID = %s;"
            self.open()
            self.stmt.execute(query, (customer_id,))
            customer_data = self.stmt.fetchone()

            if customer_data:
                print("--Customer found by ID:--")
                print(customer_data)
                return customer_data
            else:
                self.close()
                raise CustomException("Customer not found")

        except CustomException as e:
            print(e)
        except Exception as e:
            print(str(e) + "---Error getting customer by ID:--")

    def GetCustomerByUsername(self):
        try:
            username = input("enter username name:")
            query = "SELECT * FROM Customer WHERE Username = %s;"
            self.open()
            self.stmt.execute(query, (username,))
            customer_data = self.stmt.fetchone()

            if customer_data:
                print("--Customer found by username:--")
                print(customer_data)
            else:
                raise CustomException("Customer not found")

            self.close()
        except CustomException as e:
            print(e)
        except Exception as e:
            print(str(e) + "---Error getting customer by username:--")

    def authenticate_customer(self):
        try:
            customer_id = int(input("Enter Customer ID: "))
            password = input("Enter Password: ")
            query = "SELECT Password FROM Customer WHERE CustomerID = %s;"
            self.open()
            self.stmt.execute(query, (customer_id,))
            stored_password = self.stmt.fetchone()

            if stored_password:
                stored_password = stored_password[0]
                hashed_input_password = custom_hash_password(password)
                if stored_password == hashed_input_password:
                    print("Authentication successful. Welcome!")
                else:
                    raise AuthenticationException()
            
            else:
                raise CustomException("Customer with ID does not exists")

            self.close()
        except CustomException as e:
            print(e)
        except AuthenticationException as e:
            print(e)
            return e
        except ValueError:
            print("Please enter a valid integer for Customer ID.")
        except Exception as e:
            print(str(e) + "---Error during authentication:--")
