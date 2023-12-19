from datetime import date


class Reservation:
    def __init__(self, reservation_id, customer_id, vehicle_id, start_date, end_date, total_cost, status):
        self.ReservationID = reservation_id
        self.CustomerID = customer_id
        self.VehicleID = vehicle_id
        self.StartDate = start_date
        self.EndDate = end_date
        self.TotalCost = total_cost
        self.Status = status

    def CalculateTotalCost(self):
        pass


reservation1 = Reservation(1, 101, 201, date(2023, 1, 1), date(2023, 1, 5), 0, "Pending")
