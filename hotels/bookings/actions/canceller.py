from ...models import Booking

class BookingCanceller:
    def __init__(self, booking):
        self.booking = booking

    def cancel(self):
        self.booking.status = Booking.BookingStatus.CANCELLED
        self.booking.save()
