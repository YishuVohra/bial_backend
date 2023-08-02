from django.urls import path
from rest_framework import routers

from shift.views import CreateShiftAPIView, FetchAllShiftsAPIView, UpdateShiftAPIView



router = routers.DefaultRouter()

urlpatterns = [
    path('create_shift/', CreateShiftAPIView.as_view(), name='create_shift'),
    path('fetch_all_shifts/', FetchAllShiftsAPIView.as_view(), name='fetch_all_shifts'),
    path('update_shift/', UpdateShiftAPIView.as_view(), name='update_shift'),
]

urlpatterns += router.urls