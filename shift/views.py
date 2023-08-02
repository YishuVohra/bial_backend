from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound, ValidationError, NotAcceptable
from shift.models import Shift

from shift.serializers import CreateShiftSerializer, ShiftSerializer




class CreateShiftAPIView(CreateAPIView):
    serializer_class = CreateShiftSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(context={'request':request})
        resp = serializer.create_shift(validated_data=request.data)
        return Response(resp, status=status.HTTP_201_CREATED)
    


class FetchAllShiftsAPIView(ListAPIView):
    serializer_class = ShiftSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Shift.objects.all()

        return queryset
    


class UpdateShiftAPIView(UpdateAPIView):
    permission_classes = (AllowAny,)

    def put(self, request, *args, **kwargs):
        shift_id = request.data.get('shift_id')

        if shift_id == "null" or shift_id == '':
            shift_id = None

        shift_obj = Shift.objects.filter(id = shift_id).last()
        if not shift_obj:
            raise NotFound({
                'message':'This Shift does not exists.'
            })
        
        if request.data.get('name'):
            shift_obj.name = request.data['name']
        if request.data.get('description'):
            shift_obj.description = request.data['description']
        if request.data.get('start_time'):
            shift_obj.start_time = request.data['start_time']
        if request.data.get('end_time'):
            shift_obj.end_time = request.data['end_time']
        if request.data.get('duration_in_hrs'):
            shift_obj.duration_in_hrs = request.data['duration_in_hrs']
        if request.data.get('min_staff_required'):
            shift_obj.min_staff_required = request.data['min_staff_required']
        if request.data.get('max_staff_allowed'):
            shift_obj.max_staff_allowed = request.data['max_staff_allowed']

        shift_obj.save()
            

        return Response({"message": "Shift Updated Successfully !!"}, status=200)