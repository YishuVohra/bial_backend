from rest_framework import serializers
from rest_framework.exceptions import ParseError, NotFound, ValidationError, NotAcceptable

from shift.models import Shift




class CreateShiftSerializer(serializers.ModelSerializer):

    def create_shift(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        start_time = validated_data.get('start_time')
        end_time = validated_data.get('end_time')
        duration_in_hrs = validated_data.get('duration_in_hrs')
        min_staff_required = validated_data.get('min_staff_required')
        max_staff_allowed = validated_data.get('max_staff_allowed')

        shift_obj = Shift.objects.create(name= name, description= description, start_time= start_time, end_time= end_time, duration_in_hrs= duration_in_hrs, min_staff_required= min_staff_required, max_staff_allowed= max_staff_allowed)


        return {
                'message':'Shift details added successfully !!'
            }    



class ShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = '__all__'