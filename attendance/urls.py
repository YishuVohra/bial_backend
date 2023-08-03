from django.urls import path
from rest_framework import routers

from attendance.views import FetchAllAttendancesAPIView, UpdateAttendanceAPIView



router = routers.DefaultRouter()

urlpatterns = [
    path('fetch_all_attendances/', FetchAllAttendancesAPIView.as_view(), name='fetch_all_attendances'),
    path('update_attendance/', UpdateAttendanceAPIView.as_view(), name='update_attendance'),
]

urlpatterns += router.urls