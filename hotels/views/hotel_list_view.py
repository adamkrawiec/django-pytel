from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Hotel
from ..serializers import HotelSerializer

class HotelListView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the hotels
        '''
        hotels = Hotel.objects.prefetch_related('city').all()
        serializer_context = {
            'request': request,
        }
        serializer = HotelSerializer(hotels, many=True, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)