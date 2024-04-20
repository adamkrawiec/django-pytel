from django.test import TestCase, Client
from django.urls import reverse
import json
from hotels.models import City, Hotel

class HotelsListTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.city = City.objects.create(name="New York")
        self.hotel = Hotel.objects.create(name="Hotel New York", city=self.city)
    
    def tearDown(self):
        City.objects.all().delete()
        Hotel.objects.all().delete()
  
    def test_get_hotels_endpoint(self):
        """
        Runs a GET request to hotels endpoint and checks if the response is 200 OK
        """
        response = self.client.get(reverse("hotels_list"))
        response_data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response_data), 1)

        self.assertEqual(response_data[0]["name"], "Hotel New York")
        self.assertEqual(response_data[0]["city"]["name"], "New York")
        self.assertEqual(response_data[0]["url"], f"/hotels/{self.hotel.id}")
        self.assertEqual(response_data[0]["rooms"], [])