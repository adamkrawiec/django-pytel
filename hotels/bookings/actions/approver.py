from ...models import Booking

class BookingApprover:
    def __init__(self, booking):
        self.booking = booking

    def approve(self):
        self.booking.status = Booking.BookingStatus.APPROVED
        self.booking.save()
