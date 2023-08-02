from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from user.serializers import EmployeeRegistrationSerializer, LoginSerializer
from common.views import DataWrapperViewSet, GenericAPIView




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
