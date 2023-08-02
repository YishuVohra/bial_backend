from django.urls import path
from rest_framework import routers
from .views import EmployeeRegistrationAPIView, LoginAPIView


router = routers.DefaultRouter()

urlpatterns = [
    path('register_employee/', EmployeeRegistrationAPIView.as_view(), name='register_employee'),
    path('login/', LoginAPIView.as_view(), name='login'),
]

urlpatterns += router.urls
