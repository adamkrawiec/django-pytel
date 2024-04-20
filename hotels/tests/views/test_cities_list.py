from django.test import TestCase, Client
from django.urls import reverse
import json
from hotels.models import City

class CitiesListTest(TestCase):
    def setUp(self):
        self.client = Client()
        City.objects.create(name="New York")

    def test_get_cities_endpoint(self):
        """
        Runs a GET request to hotels/cities endpoint and checks if the response is 200 OK
        """
        response = self.client.get(reverse("cities_list"))

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(len(response_data), 1)