from django.urls import path
from rest_framework import routers

from employee.views import AddFamilyAPIView, FetchAllEmployeesProfileApiView, FetchEmployeeProfileApiView, UpdateEmployeeProfileAPIView


router = routers.DefaultRouter()

urlpatterns = [
    path('fetch_employee_profile/', FetchEmployeeProfileApiView.as_view(), name='fetch_employee_profile'),
    path('update_employee_profile/', UpdateEmployeeProfileAPIView.as_view(), name='update_employee_profile'),
    path('fetch_all_employees_profile/', FetchAllEmployeesProfileApiView.as_view(), name='fetch_all_employees_profile'),
    path('add_family/', AddFamilyAPIView.as_view(), name='add_family'),
]

urlpatterns += router.urls