from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Hotel
from ..serializers import RoomSearchSerializer
from ..rooms.actions import AvailableRoomFinder
from ..utils import parse_date

class HotelSearchView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        Search hotels by city
        query params:
            city: name of the city
            check_in: date in format dd-mm-yyyy
            check_out: date in format dd-mm-yyyy
        '''
        city_name = request.GET.get('city')
        if not city_name:
            return Response({'error': 'city is required'}, status=status.HTTP_400_BAD_REQUEST)

        check_in = parse_date(request.GET.get('check_in'))
        check_out = parse_date(request.GET.get('check_out'))

        rooms = AvailableRoomFinder(check_in, check_out).find_available_rooms_for_city(city_name)
        serializer = RoomSearchSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)