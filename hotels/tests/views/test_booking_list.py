from django.test import TestCase, Client
from django.urls import reverse
import json
from hotels.models import City, Hotel, Room, Booking

class BookingListTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.city = City.objects.create(name="New York")
        self.hotel = Hotel.objects.create(name="Hotel New York", city=self.city)
        self.room = Room.objects.create(hotel=self.hotel,daily_price=100,capacity=2)

    def tearDown(self):
        City.objects.all().delete()
        Hotel.objects.all().delete()

    def test_post_booking_endpoint(self):
        """
        Runs a POST request to hotels/booking endpoint and checks if the response is 201 Created
        """
        response = self.client.post(
            reverse("booking_list", args=(self.hotel.id, self.room.id)),
            { "check_in": "01-01-2021", "check_out": "02-01-2021" }
        )

        self.assertEqual(response.status_code, 201)
    
    def test_post_booking_endpoint_overlapping(self):
        """
        When a booking overlaps with an existing booking, the endpoint returns a 400 Bad Request
        """
        Booking(room=self.room, check_in="2021-01-01", check_out="2021-01-02").save()
        response = self.client.post(
            reverse("booking_list", args=(self.hotel.id, self.room.id)),
            { "check_in": "01-01-2021", "check_out": "02-01-2021" }
        )
        self.assertEqual(response.status_code, 400)