from rest_framework import serializers
from rest_framework.exceptions import ParseError, NotFound, ValidationError, NotAcceptable

from employee.models import EmployeeProfile, FamilyProfile
from user.serializers import UserSerializer




class EmployeeProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeProfile
        fields = '__all__'

    def get_user(self, instance):
        try:
            user = UserSerializer(instance.user).data
        except:
            user = None
        return user



class AddFamilySerializer(serializers.ModelSerializer):

    def add_family(self, validated_data):
        request_user = self.context.get('request').user
        employee_profile_obj = EmployeeProfile.objects.get(user = request_user)

        fullname = validated_data.get('fullname')
        phonenumber = validated_data.get('phonenumber')
        if phonenumber == "null" or phonenumber == '':
            phonenumber = None
        gender = validated_data.get('gender')
        profile_image = validated_data.get('profile_image')
        relationship = validated_data.get('relationship')
        is_emergency_contact = validated_data.get('is_emergency_contact')
        age_in_yrs = validated_data.get('age_in_yrs')

        if is_emergency_contact == "True" and (not phonenumber):
            raise ParseError({
                        'message':"If family is emergency contact, then phone number is required !!"
                    })
        

        family_prof_obj = FamilyProfile.objects.create(employee= employee_profile_obj, fullname= fullname, phonenumber= phonenumber, gender= gender, image= profile_image, relationship= relationship, is_emergency_contact= is_emergency_contact, age_in_yrs= age_in_yrs)


        return {
                'message':'Family details added successfully !!'
            }

