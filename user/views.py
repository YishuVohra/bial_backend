from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from user.models import User, UserPermission, UserRole

from user.serializers import CreateUserPermissionSerializer, EmployeeRegistrationSerializer, LoginSerializer, UserPermissionSerializer, UserRoleSerializer
from common.views import DataWrapperViewSet, GenericAPIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.exceptions import ParseError, NotFound, ValidationError, NotAcceptable





class EmployeeRegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    serializer_class = EmployeeRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(context={'request':request})
        resp = serializer.register_employee(validated_data=request.data)
        return Response(resp, status=status.HTTP_201_CREATED)
    
    

class LoginAPIView(GenericAPIView):
    '''
        Login API
    '''
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class()
        resp = serializer.login(data=request.data)
        return Response(resp, status=status.HTTP_200_OK)
    


class CreateUserPermissionAPIView(CreateAPIView):
    serializer_class = CreateUserPermissionSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(context={'request':request})
        resp = serializer.create_userPermission(validated_data=request.data)
        return Response(resp, status=status.HTTP_201_CREATED)
    


class FetchAllUserPermissionsAPIView(ListAPIView):
    serializer_class = UserPermissionSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = UserPermission.objects.all()

        return queryset
    


class UpdateUserPermissionAPIView(UpdateAPIView):
    permission_classes = (AllowAny,)

    def put(self, request, *args, **kwargs):
        permission_id = request.data.get('permission_id')

        if permission_id == "null" or permission_id == '':
            permission_id = None

        permission_obj = UserPermission.objects.filter(id = permission_id).last()
        if not permission_obj:
            raise NotFound({
                'message':'This Permission does not exists.'
            })
        
        if request.data.get('permission_name'):
            permission_obj.permission_name = request.data['permission_name']
        if request.data.get('permission_desc'):
            permission_obj.permission_desc = request.data['permission_desc']

        permission_obj.save()
            

        return Response({"message": "Permission Updated Successfully !!"}, status=200)
    


class ResetPasswordAPIView(UpdateAPIView):
    permission_classes = (AllowAny,)

    def put(self, request, *args, **kwargs):
        username = request.data.get('user')
        user_obj = User.objects.filter(Q(username=username) | Q(email=username) | Q(phonenumber=username)).first()
        if user_obj is None:
            raise NotFound({
                        'message':"An user with this username does not exists !!"
                    })
        
        data = request.data
        password = data['password']
        user_obj.set_password(password)
        user_obj.save()


        return Response({"message": "Password Reset Done Successfully !!"}, status=200)
    


class FetchAllUserRolesAPIView(ListAPIView):
    serializer_class = UserRoleSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = UserRole.objects.all()

        return queryset
