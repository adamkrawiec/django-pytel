from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from ..models import Booking
from ..bookings.actions import BookingApprover, BookingCanceller

class BookingDetailView(APIView):
    def get(self, request, booking_id, *args, **kwargs):
        '''
        Get a booking
        '''
        return Response({}, status=status.HTTP_200_OK)

    def patch(self, request, booking_id, *args, **kwargs):
        '''
        Update a booking
        '''
        try:
            booking = Booking.objects.get(pk=booking_id)
            if request.data.get('booking_status').lower() == 'approved':
                BookingApprover(booking).approve()
            else:
                BookingCanceller(booking).cancel()
            return Response({}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise Http404