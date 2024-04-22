from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Room
from ..serializers import RoomSerializer
from ..rooms.actions import AvailableRoomFinder
from ..utils import parse_date

class HotelRoomsListView(APIView):
    def get(self, request, hotel_id, *args, **kwargs):
        '''
        Get the list of rooms for a hotel
        query params:
            check_in_at: date in format dd-mm-yyyy
            check_out_at: date in format dd-mm-yyyy
        '''
        check_in = parse_date(request.GET.get('check_in'))
        check_out = parse_date(request.GET.get('check_out'))

        rooms = AvailableRoomFinder(check_in, check_out).find_available_rooms_for_hotel(hotel_id)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)