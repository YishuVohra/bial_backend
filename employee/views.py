from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound, ValidationError, NotAcceptable
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView

from employee.models import EmployeeProfile
from employee.serializers import AddFamilySerializer, EmployeeProfileSerializer
from team.models import Team
from user.models import User




class FetchEmployeeProfileApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        request_user = self.request.user

        queryset = EmployeeProfile.objects.get(user = request_user)

        return Response(
            EmployeeProfileSerializer(queryset).data
        )
    


class UpdateEmployeeProfileAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        request_user = self.request.user

        user_obj = User.objects.all()
        employee_profile_obj = EmployeeProfile.objects.get(user = request_user)

        if request.data.get('username'):
            if user_obj.filter(username = request.data['username']):
                raise ValidationError({
                        'message':"This username already exists !!"
                    })
            employee_profile_obj.user.username = request.data['username']

        if request.data.get('email'):
            if user_obj.filter(email = request.data['email']):
                raise ValidationError({
                        'message':"This email ID already exists !!"
                    })
            employee_profile_obj.user.email = request.data['email']

        if request.data.get('gender'):
            employee_profile_obj.user.gender = request.data['gender']

        if request.data.get('phonenumber'):
            if user_obj.filter(phonenumber = request.data['phonenumber']):
                raise ValidationError({
                        'message':"This phone number already exists !!"
                    })
            employee_profile_obj.user.phonenumber = request.data['phonenumber']

        if request.data.get('fullname'):
            employee_profile_obj.user.fullname = request.data['fullname']
        if request.data.get('father_name'):
            employee_profile_obj.father_name = request.data['father_name']
        if request.data.get('marital_status'):
            employee_profile_obj.marital_status = request.data['marital_status']
        if request.data.get('profile_image'):
            employee_profile_obj.image = request.data['profile_image']
        if request.data.get('date_of_birth'):
            employee_profile_obj.date_of_birth = request.data['date_of_birth']
        if request.data.get('team_id'):
            team_obj = Team.objects.filter(id = request.data['team_id']).last()
            employee_profile_obj.team = team_obj

        employee_profile_obj.user.save()
        employee_profile_obj.save()

        return Response({"message": "Updated Profile Details Successfully"}, status=200)
    


class AddFamilyAPIView(APIView):
    serializer_class = AddFamilySerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(context={'request':request})
        resp = serializer.add_family(validated_data=request.data)
        return Response(resp, status=status.HTTP_201_CREATED)
