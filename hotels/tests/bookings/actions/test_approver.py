from django.test import TestCase
from hotels.models import City, Hotel, Room, Booking
from hotels.bookings.actions import BookingApprover

class BookingApproverTest(TestCase):
    def setUp(self):
        self.city = City.objects.create(name="New York")
        self.hotel = Hotel.objects.create(name="Hotel New York", city=self.city)
        self.room = Room.objects.create(hotel=self.hotel,daily_price=100,capacity=2)
        self.booking = Booking.objects.create(room=self.room, check_in="2021-01-01", check_out="2021-01-02")
    
    def test_approve(self):
        """
        Changes booking status to APPROVED
        """
        BookingApprover(self.booking).approve()
        self.assertEqual(self.booking.status, Booking.BookingStatus.APPROVED)