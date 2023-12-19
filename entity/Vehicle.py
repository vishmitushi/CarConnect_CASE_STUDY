class Vehicle:
    def __init__(self, vehicle_id, model, make, year, color, registration_number, availability, daily_rate):
        self.VehicleID = vehicle_id
        self.Model = model
        self.Make = make
        self.Year = year
        self.Color = color
        self.RegistrationNumber = registration_number
        self.Availability = availability
        self.DailyRate = daily_rate


vehicle1 = Vehicle(1, "sedan", "tata", 2002, "blue", "ap0243", False, 40)
