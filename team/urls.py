from django.urls import path
from rest_framework import routers

from team.views import CreateTeamAPIView, FetchAllTeamsAPIView, UpdateTeamAPIView




router = routers.DefaultRouter()

urlpatterns = [
    path('create_team/', CreateTeamAPIView.as_view(), name='create_team'),
    path('fetch_all_teams/', FetchAllTeamsAPIView.as_view(), name='fetch_all_teams'),
    path('update_team/', UpdateTeamAPIView.as_view(), name='update_team'),
]

urlpatterns += router.urls