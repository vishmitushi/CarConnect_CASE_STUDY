
class ReservationException(Exception):
    def __init__(self, message="Vehicle already booked.Try another date"):
        self.message = message
        super().__init__(self.message)
