from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import City
from ..serializers import CitySerializer

class CityListView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the cities
        '''
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({ "cities": serializer.data }, status=status.HTTP_200_OK)