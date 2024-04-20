from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Room
from ..serializers import RoomSerializer

class RoomDetailView(APIView):
    def get(self, request, hotel_id, room_id, *args, **kwargs):
        '''
        Get the room details
        '''
        room = Room.objects.get(pk=room_id)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)