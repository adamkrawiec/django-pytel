from django.urls import path
from .views import(
    HotelListView,
    HotelSearchView,
    HotelDetailView,
    CityListView,
    CityDetailView,
    RoomDetailView,
    BookingListView,
    HotelRoomsListView
)

urlpatterns = [
    path('', HotelListView.as_view(), name='hotels_list'),
    path('search', HotelSearchView.as_view(), name='hotel_search'),
    path('<int:hotel_id>', HotelDetailView.as_view(), name='hotel_detail'),
    path('cities', CityListView.as_view(), name='cities_list'),
    path('cities/<int:city_id>', CityDetailView.as_view(), name='city_detail'),
    path('<int:hotel_id>/rooms', HotelRoomsListView.as_view(), name='hotel_rooms_list'),
    path('<int:hotel_id>/rooms/<int:room_id>', RoomDetailView.as_view(), name='room_detail'),
    path('<int:hotel_id>/rooms/<int:room_id>/bookings', BookingListView.as_view(), name='booking_list'),
]