from django.urls import path
from rest_framework import routers
from .views import CreateUserPermissionAPIView, EmployeeRegistrationAPIView, FetchAllUserPermissionsAPIView, LoginAPIView, ResetPasswordAPIView, UpdateUserPermissionAPIView


router = routers.DefaultRouter()

urlpatterns = [
    path('register_employee/', EmployeeRegistrationAPIView.as_view(), name='register_employee'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('create_permission/', CreateUserPermissionAPIView.as_view(), name='create_permission'),
    path('fetch_all_permissions/', FetchAllUserPermissionsAPIView.as_view(), name='fetch_all_permissions'),
    path('update_permission/', UpdateUserPermissionAPIView.as_view(), name='update_permission'),
    path('reset_password/', ResetPasswordAPIView.as_view(), name='reset_password'),
]

urlpatterns += router.urls
