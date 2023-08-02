from django.urls import path
from rest_framework import routers

from team.views import CreateDepartmentAPIView, CreateTeamAPIView, FetchAllDepartmentsAPIView, FetchAllTeamsAPIView, UpdateDepartmentAPIView, UpdateTeamAPIView




router = routers.DefaultRouter()

urlpatterns = [
    path('create_department/', CreateDepartmentAPIView.as_view(), name='create_department'),
    path('fetch_all_departments/', FetchAllDepartmentsAPIView.as_view(), name='fetch_all_departments'),
    path('update_department/', UpdateDepartmentAPIView.as_view(), name='update_department'),
    path('create_team/', CreateTeamAPIView.as_view(), name='create_team'),
    path('fetch_all_teams/', FetchAllTeamsAPIView.as_view(), name='fetch_all_teams'),
    path('update_team/', UpdateTeamAPIView.as_view(), name='update_team'),
]

urlpatterns += router.urls