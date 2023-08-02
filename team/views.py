from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound, ValidationError, NotAcceptable

from team.models import Department, Team
from team.serializers import CreateTeamSerializer, TeamSerializer





class CreateTeamAPIView(CreateAPIView):
    serializer_class = CreateTeamSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(context={'request':request})
        resp = serializer.create_team(validated_data=request.data)
        return Response(resp, status=status.HTTP_201_CREATED)
    


class FetchAllTeamsAPIView(ListAPIView):
    serializer_class = TeamSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Team.objects.all()

        return queryset
    


class UpdateTeamAPIView(UpdateAPIView):
    permission_classes = (AllowAny,)

    def put(self, request, *args, **kwargs):
        team_id = request.data.get('team_id')

        if team_id == "null" or team_id == '':
            team_id = None

        team_obj = Team.objects.filter(id = team_id).last()
        if not team_obj:
            raise NotFound({
                'message':'This Team does not exists.'
            })
        
        if request.data.get('name'):
            team_obj.name = request.data['name']
        if request.data.get('description'):
            team_obj.description = request.data['description']
        if request.data.get('department_id'):
            department_obj = Department.objects.filter(id = request.data['department_id']).last()
            team_obj.department = department_obj
        if request.data.get('contact_info'):
            team_obj.contact_info = request.data['contact_info']

        team_obj.save()
            

        return Response({"message": "Team Updated Successfully !!"}, status=200)