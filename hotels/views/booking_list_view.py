from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Booking, Room
from ..serializers import BookingSerializer, RoomSerializer
from ..bookings.actions.create import BookingCreateAction

from datetime import datetime

class BookingListView(APIView):
    def get(self, request, hotel_id, room_id, *args, **kwargs):
        '''
        Get the list of bookings for a room
        '''
        bookings = Booking.objects.filter(room_id=room_id)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, hotel_id, room_id, *args, **kwargs):
        '''
        Create a booking for a room
        '''
        check_in = datetime.strptime(request.data.get('check_in'), '%d-%m-%Y')
        check_out = datetime.strptime(request.data.get('check_out'), '%d-%m-%Y')
        serializer = BookingCreateAction(room_id, check_in, check_out).execute()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)