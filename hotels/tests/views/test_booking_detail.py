from django.test import TestCase, Client
from django.urls import reverse
import json
from hotels.models import City, Hotel, Room, Booking

class BookingDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.city = City.objects.create(name="New York")
        self.hotel = Hotel.objects.create(name="Hotel New York", city=self.city)
        self.room = Room.objects.create(hotel=self.hotel,daily_price=100,capacity=2)
        self.booking = Booking.objects.create(room=self.room, check_in="2021-01-01", check_out="2021-01-02")

    def tearDown(self):
        City.objects.all().delete()
        Hotel.objects.all().delete()

    def test_patch_marks_booking_as_approved(self):
        """
        Runs a PATCH request to hotels/booking/<booking_id> endpoint and checks if the response is 200 OK
        """
        response = self.client.patch(
            reverse("booking_detail", args=(self.booking.id,)),
            { "booking_status": "APPROVED" },
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, Booking.BookingStatus.APPROVED)
    
    def test_patch_marks_booking_as_cancelled(self):
        """
        Runs a PATCH request to hotels/booking/<booking_id> endpoint and checks if the response is 200 OK
        """
        response = self.client.patch(
            reverse("booking_detail", args=(self.booking.id,)),
            { "booking_status": "cancelled" },
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, Booking.BookingStatus.CANCELLED)
    
    def test_patch_when_booking_not_found(self):
        """
        Runs a PATCH request to hotels/booking/<booking_id> endpoint and checks if the response is 404 Not Found
        """
        response = self.client.patch(
            reverse("booking_detail", args=(99,)),
            { "booking_status": "cancelled" },
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 404)