from .overlaps import BookingOverlaps

class BookingValidator:
    def __init__(self, booking):
        self.booking = booking
    
    def is_valid(self):
        return not BookingOverlaps().overlapping_bookings(self.booking.room_id, self.booking.check_in, self.booking.check_out).exists()