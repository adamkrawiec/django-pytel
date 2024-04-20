from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Room
from ..serializers import RoomSerializer
from datetime import datetime

class HotelRoomsListView(APIView):
	def get(self, request, hotel_id, *args, **kwargs):
		'''
		Get the list of rooms for a hotel
        query params:
            check_in_at: date in format dd-mm-yyyy
            check_out_at: date in format dd-mm-yyyy
		'''
		query = {}
		if request.GET.get('check_in_at'):
			query['booking__check_in__gte'] = datetime.strptime(request.GET.get('check_in_at'), '%d-%m-%Y')
		if request.GET.get('check_out_at'):
			query['booking__check_out__lte'] = datetime.strptime(request.GET.get('check_out_at'), '%d-%m-%Y')

		rooms = Room.objects.filter(hotel_id=hotel_id).exclude(**query)
		serializer = RoomSerializer(rooms, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)