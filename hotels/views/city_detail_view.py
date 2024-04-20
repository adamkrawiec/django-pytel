from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import City
from ..serializers import CitySerializer

class CityDetailView(APIView):
    def get(self, request, city_id, *args, **kwargs):
        '''
        Get the city details
        '''
        city = City.objects.get(pk=city_id)
        serializer = CitySerializer(city)
        return Response(serializer.data, status=status.HTTP_200_OK)
