from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Hotel
from ..serializers import HotelSerializer

class HotelDetailView(APIView):
    def get(self, request, hotel_id, *args, **kwargs):
        '''
        Get the hotel details
        '''
        serializer_context = {
            'request': request,
        }

        hotel = Hotel.objects.prefetch_related('city', 'room_set').get(pk=hotel_id)
        serializer = HotelSerializer(hotel, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)
