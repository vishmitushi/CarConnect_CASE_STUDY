from dao.CustomerService import custom_hash_password
from entity.IAdminService import IAdminService
from exception.AdminNotFoundException import AdminNotFoundException
from exception.AuthenticationException import AuthenticationException
from exception.CustomException import CustomException, StringCheck, validate_email, validate_phone
from util.DBConnUtil import dbConnection

class AdminService(IAdminService,dbConnection):

    def create_class(self):
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS Admin (
                AdminID INT PRIMARY KEY AUTO_INCREMENT,
                FirstName VARCHAR(55),
                LastName VARCHAR(55),
                Email VARCHAR(55),
                PhoneNumber CHAR(12),
                Username VARCHAR(55) UNIQUE,
                Password VARCHAR(255),
                Role ENUM('super admin', 'fleet manager'),
                JoinDate DATE
            );
            """
            self.open()
            self.stmt.execute(create_table_query)
            self.conn.commit()
            print("--Table 'Admin' created successfully:--")
            self.close()
        except Exception as e:
            print(str(e) + "---Error creating table 'Admin':--")

    def RegisterAdmin(self):
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

            username = input("Enter Username: ")
            if not isinstance(username, str):
                raise CustomException("Enter string only")
            StringCheck(username)
            self.username = username

            password = input("Enter Password: ")
            self.password = custom_hash_password(password)

            role = input("Enter Role (super admin/fleet manager): ").lower()
            if role not in ['super admin', 'fleet manager']:
                raise CustomException("Enter valid role")
            self.role = role

            join_date = input("Enter Join Date (YYYY-MM-DD): ")
            self.join_date = join_date

            insert_query = """
            INSERT INTO Admin (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
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
                    self.username,
                    self.password,
                    self.role,
                    self.join_date,
                ),
            )
            self.conn.commit()
            print("--Admin added successfully:--")
            self.close()

        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error adding admin:--")

    def select(self):
        try:
            select_query = """
            SELECT * FROM Admin;
            """
            self.open()
            self.stmt.execute(select_query)
            data = self.stmt.fetchall()
            if data:
                print("-- Admin Data --")
                for row in data:
                    print(f"\nAdminID: {row[0]},\n FirstName: {row[1]},\n LastName: {row[2]},\n Email: {row[3]}, "
                          f"\nPhoneNumber: {row[4]},\n Username: {row[5]},\n Password: {row[6]},\n Role: {row[7]}, "
                          f"\nJoinDate: {row[8]}")
            else:
                print("-- No admins found in the database --")
            self.close()
        except Exception as e:
            print(str(e) + "---Error selecting data from 'Admin':--")

    def UpdateAdmin(self):
        try:
            self.select()
            admin_id = int(input("Enter Admin ID to be updated: "))
            if not isinstance(admin_id, int) or admin_id < 0:
                raise CustomException("Enter a positive integer for Admin ID only")
            self.admin_id = int(admin_id)

            update_query = "UPDATE Admin SET "
            data = []

            first_name = input("Enter First Name (Press Enter to skip): ")
            if first_name:
                StringCheck(first_name)
                update_query += "FirstName=%s, "
                data.append(first_name)

            last_name = input("Enter Last Name (Press Enter to skip): ")
            if last_name:
                StringCheck(last_name)
                update_query += "LastName=%s, "
                data.append(last_name)

            email = input("Enter Email (Press Enter to skip): ")
            if email:
                validate_email(email)
                update_query += "Email=%s, "
                data.append(email)

            phone_number = input("Enter Phone Number (Press Enter to skip): ")
            if phone_number:
                validate_phone(phone_number)
                update_query += "PhoneNumber=%s, "
                data.append(phone_number)

            username = input("Enter Username (Press Enter to skip): ")
            if username:
                StringCheck(username)
                update_query += "Username=%s, "
                data.append(username)

            password = input("Enter Password (Press Enter to skip): ")
            print(password)
            if password:
                hashed_password = custom_hash_password(password)
                print(hashed_password)
                update_query += "Password=%s, "
                data.append(hashed_password)
                print(data)

            role = input("Enter Role (Press Enter to skip): ").lower()
            if role and role in ['super admin', 'fleet manager']:
                update_query += "Role=%s, "
                data.append(role)

            join_date = input("Enter Join Date (YYYY-MM-DD) (Press Enter to skip): ")
            if join_date:
                update_query += "JoinDate=%s, "
                data.append(join_date)

            if not data:
                print("No fields provided for update.")
                return

            update_query = update_query.rstrip(', ')
            update_query += " WHERE AdminID=%s"
            data.append(self.admin_id)

            self.open()
            self.stmt.execute(update_query, tuple(data))
            self.conn.commit()
            print('Admin record updated successfully.')
            self.close()

        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error updating admin:--")

    def DeleteAdmin(self):
        try:
            admin_id = int(input("Enter Admin ID to be deleted: "))
            if not isinstance(admin_id, int) or admin_id < 0:
                raise CustomException("Enter a positive integer for Admin ID only")

            delete_query = "DELETE FROM Admin WHERE AdminID = %s"

            self.open()
            self.stmt.execute(delete_query, (admin_id,))
            self.conn.commit()
            print(f"Admin with ID {admin_id} deleted successfully.")
            self.close()

        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error deleting admin:--")

    def GetAdminById(self):
        try:
            admin_id = int(input("enter ID :"))
            query = "SELECT * FROM Admin WHERE AdminID = %s;"
            self.open()
            self.stmt.execute(query, (admin_id,))
            customer_data = self.stmt.fetchone()

            if customer_data:
                print("--Customer found by ID:--")
                print(customer_data)
            else:
                raise AdminNotFoundException()

            self.close()
        except AdminNotFoundException as e:
            print(e)
        except Exception as e:
            print(str(e) + "---Error getting customer by ID:--")

    def GetAdminByUsername(self):
        try:
            username = input("Enter username: ")
            query = "SELECT * FROM Admin WHERE Username = %s;"
            self.open()
            self.stmt.execute(query, (username,))
            admin_data = self.stmt.fetchone()
            if admin_data:
                print("-- Admin found by username:--")
                print(admin_data)
            else:
                raise AdminNotFoundException()
            self.close()
        except AdminNotFoundException as e:
            print(e)
        except Exception as e:
            print(str(e) + "---Error getting admin by username:--")

    def authenticate_password(self):
        try:
            username = int(input("Enter Username: "))
            password = input("Enter Password: ")
            print(password)
            query = "SELECT Password FROM Admin WHERE AdminID = %s;"
            self.open()
            self.stmt.execute(query, (username,))
            stored_password = self.stmt.fetchone()

            if stored_password:
                stored_password = stored_password[0]  # Extract the hashed password from the tuple
                print(stored_password)
                # Hash the entered password for comparison
                entered_password_hash = custom_hash_password(password)
                print(entered_password_hash)
                # Compare the stored and entered password hashes
                if stored_password == entered_password_hash:
                    print("Authentication successful. Welcome, {}!".format(username))
                else:
                    raise AuthenticationException()
            else:
                print("User with username {} not found.".format(username))

            self.close()
        except AuthenticationException as e:
            print(e)
        except Exception as e:
            print(str(e) + "---Error during password authentication:--")
