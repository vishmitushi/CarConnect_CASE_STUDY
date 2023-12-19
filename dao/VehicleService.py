from entity.IVehicleService import IVehicleService
from exception.CustomException import CustomException, StringCheck
from exception.VehicleNotFoundException import VehicleNotFoundException
from util.DBConnUtil import dbConnection


class VehicleService(IVehicleService ,dbConnection):

    def create_class(self):
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS Vehicle (
                VehicleID INT PRIMARY KEY AUTO_INCREMENT,
                Model VARCHAR(55),
                Make VARCHAR(55),
                Year INT,
                Color VARCHAR(55),
                RegistrationNumber VARCHAR(20) UNIQUE,
                Availability BOOLEAN,
                DailyRate DECIMAL(6, 2)
            );
            """
            self.open()
            self.stmt.execute(create_table_query)
            self.conn.commit()
            print("--Table 'Vehicle' created successfully:--")
            self.close()
        except Exception as e:
            print(str(e) + "---Error creating table 'Vehicle':--")

    def AddVehicle(self):
        try:
            model = input("Enter Model: ")
            if not isinstance(model, str):
                raise CustomException("Enter string only")
            StringCheck(model)
            self.model = model

            make = input("Enter Make: ")
            if not isinstance(make, str):
                raise CustomException("Enter string only")
            StringCheck(make)
            self.make = make

            year = int(input("Enter Year: "))
            if not isinstance(year, int) or year < 0:
                raise CustomException("Enter positive integer only")
            self.year = int(year)

            color = input("Enter Color: ")
            if not isinstance(color, str):
                raise CustomException("Enter string only")
            StringCheck(color)
            self.color = color

            registration_number = input("Enter Registration Number: ")
            if not isinstance(registration_number, str):
                raise CustomException("Enter string only")
            self.registration_number = registration_number

            availability = input("Enter Availability (True/False): ").lower()
            if availability not in ['true', 'false']:
                raise CustomException("Enter True or False only")
            self.availability = availability == 'true'

            daily_rate = float(input("Enter Daily Rate: "))
            if not isinstance(daily_rate, (int, float)):
                raise CustomException("Enter integer or float only")
            self.daily_rate = float(daily_rate)

            insert_query = """
            INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            self.open()
            self.stmt.execute(
                insert_query,
                (
                    self.model,
                    self.make,
                    self.year,
                    self.color,
                    self.registration_number,
                    self.availability,
                    self.daily_rate,
                ),
            )
            self.conn.commit()
            print("--Vehicle added successfully:--")
            self.close()
            return f'Vehicle added successfully'
        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error adding vehicle:--")

    def GetAvailableVehicles(self):
        try:
            select_query = """
            SELECT * FROM Vehicle;
            """
            self.open()
            self.stmt.execute(select_query)
            data = self.stmt.fetchall()

            if data:
                print("-- Vehicle Data --")
                for row in data:
                    print(f"\nVehicleID: {row[0]},\n Model: {row[1]},\n Make: {row[2]},\n Year: {row[3]}, "
                          f"\nColor: {row[4]},\n RegistrationNumber: {row[5]},\n Availability: {row[6]}, "
                          f"\nDailyRate: {row[7]}")
                self.close()
                return data
            else:
                raise CustomException("-- No customers found in the database --")
        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error selecting data from 'Vehicle':--")

    def CountofVehicles(self):
        try:
            select_query = """
            SELECT COUNT(*) FROM Vehicle;
            """
            self.open()
            self.stmt.execute(select_query)
            data = self.stmt.fetchall()
            if data:
                return data
            else:
                raise CustomException("-- No Vehicles found in the database --")
        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error selecting data from 'Vehicle':--")

    def UpdateVehicle(self):
        try:
            self.GetAvailableVehicles()
            vehicle_id = int(input('Enter Vehicle ID to be Updated: '))
            if vehicle_id < 0:
                raise CustomException("ID should be positive")
            update_vehicle_str = 'UPDATE Vehicle SET '
            data = []

            self.model = input('Enter Model (Press Enter to skip): ')
            if self.model:
                if not isinstance(self.model, str):
                    raise CustomException("Enter string only")
                StringCheck(self.model)
                self.model = self.model
                update_vehicle_str += 'Model=%s, '
                StringCheck(self.model)
                data.append(self.model)

            self.make = input('Enter Make (Press Enter to skip): ')
            if self.make:
                if not isinstance(self.make, str):
                    raise CustomException("Enter string only")
                StringCheck(self.make)
                self.make = self.make
                update_vehicle_str += 'Make=%s, '
                StringCheck(self.make)
                data.append(self.make)

            self.year = input('Enter Year (Press Enter to skip): ')
            if self.year:
                self.year = int(self.year)
                if self.year < 0:
                    raise CustomException("Enter integer only")
                update_vehicle_str += 'Year=%s, '
                data.append(int(self.year))

            self.color = input('Enter Color (Press Enter to skip): ')
            if self.color:
                update_vehicle_str += 'Color=%s, '
                StringCheck(self.color)
                data.append(self.color)

            self.registration_number = input('Enter Registration Number (Press Enter to skip): ')
            if self.registration_number:
                update_vehicle_str += 'RegistrationNumber=%s, '
                data.append(self.registration_number)

            self.availability = input('Enter Availability (True/False) (Press Enter to skip): ').lower()
            if self.availability in ['true', 'false']:
                update_vehicle_str += 'Availability=%s, '
                data.append(self.availability == 'true')

            self.daily_rate = input('Enter Daily Rate (Press Enter to skip): ')
            if self.daily_rate:
                update_vehicle_str += 'DailyRate=%s, '
                data.append(float(self.daily_rate))

            if not data:
                print("No valid fields selected for update.")
            update_vehicle_str = update_vehicle_str.rstrip(', ')

            update_vehicle_str += ' WHERE VehicleID=%s'
            data.append(vehicle_id)
            self.open()
            self.stmt.execute(update_vehicle_str, data)
            self.conn.commit()
            print('Vehicle Record updated successfully.')
            return True
        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + '---Error updating vehicle details:--')

    def RemoveVehicle(self):
        try:
            vehicle_id = int(input("Enter Vehicle ID to be deleted: "))
            if not isinstance(vehicle_id, int) or vehicle_id < 0:
                raise CustomException("Enter a positive integer for Vehicle ID only")

            delete_query = "DELETE FROM Vehicle WHERE VehicleID = %s"

            self.open()
            self.stmt.execute(delete_query, (vehicle_id,))
            self.conn.commit()
            print(f"Vehicle with ID {vehicle_id} deleted successfully.")
            self.close()

        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error deleting vehicle:--")

    def GetVehicleById(self):
        try:
            vehicle_id = int(input("enter ID:"))
            query = "SELECT * FROM Vehicle WHERE VehicleID = %s;"
            self.open()
            self.stmt.execute(query, (vehicle_id,))
            vehicle_data = self.stmt.fetchone()

            if vehicle_data:
                print("--Vehicle found by ID:--")
                print(vehicle_data)
            else:
                raise VehicleNotFoundException()

            self.close()
        except VehicleNotFoundException as e:
            print(e)
        except Exception as e:
            print(str(e) + "---Error getting vehicle by ID:--")
