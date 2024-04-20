from ..models import Booking

class BookingOverlaps:
    def __init__(self, booking=None):
        self.booking = booking
  
    def overlapping_bookings(self, room_id, check_in, check_out):
        return Booking.objects.filter(
            room_id=room_id,
            check_out__gt=check_in,
            check_in__lt=check_out
        ).exclude(pk=self.booking.pk if self.booking else None)