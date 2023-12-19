from entity.IReservationService import IReservationService
from exception.CustomException import CustomException
from exception.ReservationException import ReservationException
from util.DBConnUtil import dbConnection
from datetime import datetime


class ReservationService(IReservationService,dbConnection):
    def create_table(self):
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS Reservation (
                ReservationID INT PRIMARY KEY AUTO_INCREMENT,
                CustomerID INT,
                VehicleID INT,
                StartDate DATETIME,
                EndDate DATETIME,
                TotalCost DECIMAL(6, 2),
                Status ENUM('pending', 'confirmed', 'completed'),
                FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE,
                FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID) ON DELETE CASCADE
            );
            """
            self.open()
            self.stmt.execute(create_table_query)
            self.conn.commit()
            print("--Table 'Reservation' created successfully:--")
            self.close()
            return True
        except Exception as e:
            print(str(e) + "---Error creating table 'Reservation':--")

    def CreateReservation(self):
        try:
            customer_id = int(input("Enter Customer ID: "))
            if not isinstance(customer_id, int) or customer_id < 0:
                raise CustomException("Enter positive integer only")
            self.customer_id = int(customer_id)

            vehicle_id = int(input("Enter Vehicle ID: "))
            if not isinstance(vehicle_id, int) or vehicle_id < 0:
                raise CustomException("Enter positive integer only")
            self.vehicle_id = int(vehicle_id)

            self.start_date = datetime.strptime(input("Enter Start Date (YYYY-MM-DD): "), "%Y-%m-%d")
            self.end_date = datetime.strptime(input("Enter End Date (YYYY-MM-DD): "), "%Y-%m-%d")

            total_cost = float(input("Enter Total Cost: "))
            if not isinstance(total_cost, (int, float)):
                raise CustomException("Enter positive number only")
            self.total_cost = float(total_cost)

            status = input("Enter Status (pending/confirmed/completed): ").lower()
            if status not in ['pending', 'confirmed', 'completed']:
                raise CustomException("Enter valid status")
            self.status = status
            if self.start_date>self.end_date :
                raise ReservationException()
            existing_reservations_query = "SELECT StartDate,EndDate FROM Reservation WHERE VehicleID = %s;"
            self.open()
            self.stmt.execute(existing_reservations_query, (self.vehicle_id,))
            existing_reservations = self.stmt.fetchall()
            self.close()
            if existing_reservations:
                for i in existing_reservations:
                    if i[0] < self.end_date and i[1] > self.start_date:
                        raise ReservationException()

            insert_query = """
            INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            self.open()
            self.stmt.execute(
                insert_query,
                (
                    self.customer_id,
                    self.vehicle_id,
                    self.start_date,
                    self.end_date,
                    self.total_cost,
                    self.status,
                ),
            )
            self.conn.commit()
            print("--Reservation added successfully:--")
            self.close()
        except ReservationException as e:
            print(str(e))
        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error adding reservation:--")

    def select(self):
        try:
            select_query = """
            SELECT * FROM Reservation;
            """
            self.open()
            self.stmt.execute(select_query)
            data = self.stmt.fetchall()
            if data:
                print("-- Reservation Data --")
                for row in data:
                    print(f"\nReservationID: {row[0]},\n CustomerID: {row[1]},\n VehicleID: {row[2]}, "
                          f"\nStartDate: {row[3]},\n EndDate: {row[4]},\n TotalCost: {row[5]},\n Status: {row[6]}")
            else:
                print("-- No reservations found in the database --")
            self.close()
        except Exception as e:
            print(str(e) + "---Error selecting data from 'Reservation':--")

    def UpdateReservation(self):
        try:
            self.select()
            reservation_id = int(input('Enter Reservation ID to be Updated: '))
            update_reservation_str = 'UPDATE Reservation SET '
            data = []

            self.customer_id = input('Enter Customer ID (Press Enter to skip): ')
            if self.customer_id:
                self.customer_id = int(self.customer_id)
                update_reservation_str += 'CustomerID=%s, '
                if not isinstance(self.customer_id, int) or self.customer_id < 0:
                    raise CustomException("Enter positive integer only")
                data.append(int(self.customer_id))

            self.vehicle_id = input('Enter Vehicle ID (Press Enter to skip): ')
            if self.vehicle_id:
                self.vehicle_id = int(self.vehicle_id)
                update_reservation_str += 'VehicleID=%s, '
                if not isinstance(self.vehicle_id, int) or self.vehicle_id < 0:
                    raise CustomException("Enter positive integer only")
                data.append(int(self.vehicle_id))

            self.start_date = input('Enter Start Date (YYYY-MM-DD HH:MM:SS) (Press Enter to skip): ')
            if self.start_date:
                update_reservation_str += 'StartDate=%s, '
                data.append(self.start_date)

            self.end_date = input('Enter End Date (YYYY-MM-DD HH:MM:SS) (Press Enter to skip): ')
            if self.end_date:
                update_reservation_str += 'EndDate=%s, '
                data.append(self.end_date)

            self.total_cost = input('Enter Total Cost (Press Enter to skip): ')
            if self.total_cost:
                self.total_cost = float(self.total_cost)
                update_reservation_str += 'TotalCost=%s, '
                if not isinstance(self.total_cost, (int, float)):
                    raise CustomException("Enter positive number only")
                data.append(float(self.total_cost))

            self.status = input('Enter Status (pending/confirmed/completed) (Press Enter to skip): ').lower()
            if self.status in ['pending', 'confirmed', 'completed']:
                update_reservation_str += 'Status=%s, '
                data.append(self.status)

            if not data:
                print("No valid fields selected for update.")
                return

            update_reservation_str = update_reservation_str.rstrip(', ')

            update_reservation_str += ' WHERE ReservationID=%s'
            data.append(reservation_id)

            self.open()
            self.stmt.execute(update_reservation_str, data)
            self.conn.commit()
            print('Reservation Record updated successfully.')

        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + '---Error updating reservation details:--')

    def CancelReservation(self):
        try:
            reservation_id = int(input("Enter Reservation ID to be deleted: "))
            if not isinstance(reservation_id, int) or reservation_id < 0:
                raise CustomException("Enter a positive integer for Reservation ID only")

            delete_query = "DELETE FROM Reservation WHERE ReservationID = %s"

            self.open()
            self.stmt.execute(delete_query, (reservation_id,))
            self.conn.commit()
            print(f"Reservation with ID {reservation_id} deleted successfully.")
            self.close()

        except CustomException as ce:
            print(str(ce))
        except Exception as e:
            print(str(e) + "---Error deleting reservation:--")

    def GetReservationById(self):
        try:
            reservation_id = int(input("enter reservation ID:"))
            query = "SELECT * FROM Reservation WHERE ReservationID = %s;"
            self.open()
            self.stmt.execute(query, (reservation_id,))
            reservation_data = self.stmt.fetchone()

            if reservation_data:
                print("--Reservation found by ID:--")
                print(reservation_data)
            else:
                self.close()
                CustomException("Reservation details not found")
        except CustomException as e:
            print(e)
        except Exception as e:
            print(str(e) + "---Error getting reservation by ID:--")

    def GetReservationsByCustomerId(self):
        try:
            customer_id = int(input("enter customer ID:"))
            query = "SELECT * FROM Reservation WHERE CustomerID = %s;"
            self.open()
            self.stmt.execute(query, (customer_id,))
            reservations_data = self.stmt.fetchall()

            if reservations_data:
                print("--Reservations found for the customer:--")
                for reservation in reservations_data:
                    print(reservation)
            else:
                self.close()
                CustomException("Reservation details not found")
        except CustomException as e:
            print(e)
        except Exception as e:
            print(str(e) + "---Error getting reservations by customer ID:--")