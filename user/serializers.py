import random
from rest_framework import serializers
from employee.models import EmployeeProfile
from team.models import Team
from user.models import User, UserPermission, UserRole
from rest_framework.exceptions import ParseError, NotFound, ValidationError, NotAcceptable
from django.db.models import Q




class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        allow_blank=True,
        required=False
    )
    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)


    def register_employee(self, validated_data):
        email = validated_data.get('email')
        gender = validated_data.get('gender')
        phonenumber = validated_data.get('phonenumber')
        fullname = validated_data.get('fullname')
        password = validated_data.get('password')
        role = validated_data.get('role_id')
        father_name = validated_data.get('father_name')
        marital_status = validated_data.get('marital_status')
        profile_image = validated_data.get('profile_image')
        date_of_birth = validated_data.get('date_of_birth')
        usedReferralCode = validated_data.get('usedReferralCode')
        reporting_person = validated_data.get('reporting_person_userID')
        if reporting_person == "null" or reporting_person == '':
            reporting_person = None
        team = validated_data.get('team_id')

        username = fullname.split(' ')[0].lower() + phonenumber[-4:]

        name_prefix = fullname[:4].upper()
        # Generate a random 6-character string
        random_suffix = str(random.randint(100000, 999999))
        # Combine the name prefix and random suffix to create the referral code
        referral_code = name_prefix + random_suffix


        user_obj = User.objects.filter(phonenumber = phonenumber)
        if user_obj:
            raise ValidationError({
                        'message':"User already registered with this number !!"
                    })
        
        if usedReferralCode:
            referral_code_obj = EmployeeProfile.objects.filter(shareReferralCode = usedReferralCode)
            if not referral_code_obj:
                raise ValidationError({
                        'message':"Invalid Referral Code !!"
                    })
            
        if len(password) < 8:
            raise ValidationError({
                        'message':"Password should not be less than 8 characters !!"
                    })
            
        
        user = User.objects.create(username= username, email= email, gender= gender, phonenumber= phonenumber, fullname= fullname, is_staff= True)
        user.set_password(password)
        user.save()
            

        user_role_obj = UserRole.objects.filter(id = role).last()
        reporting_person_obj = User.objects.filter(id = reporting_person).last()
        team_obj = Team.objects.filter(id = team).last()

        employee_prof_obj = EmployeeProfile.objects.create(user= user, user_group= user_role_obj, father_name= father_name, marital_status= marital_status, image= profile_image, date_of_birth= date_of_birth, shareReferralCode= referral_code, usedReferralCode= usedReferralCode, reporting_person= reporting_person_obj, team= team_obj)


        return {
                'message': 'Registration Successful !!',
                'token': user.token
            }



class LoginSerializer(serializers.Serializer):
    '''
        Serializer for login
    '''
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128, write_only=True)


    def login(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid".

        username = data.get('username', None)
        password = data.get('password', None)

        if not username:
            raise ParseError({
                        'message':"An username is required to log in !!"
                    })

        if password is None:
            raise ParseError({
                        'message':"A password is required to log in !!"
                    })
        

        # authenticate using phone number or username or email
        user = User.objects.filter(Q(username=username) | Q(email=username) | Q(phonenumber=username)).first()

        employee_obj = EmployeeProfile.objects.filter(user = user).last()

        # If no user was found matching this email/phonenumber/username/password combination then
        # it will return `None`. Raise an exception in this case.
        if user is None:
            raise NotFound({
                        'message':"An user with this username does not exists !!"
                    })

        if not user.check_password(password):
            raise ValidationError({
                        'message':"Invalid Password !!"
                    })

        if not user.is_active:
            raise ParseError({
                        'message':"This user has been deactivated !!"
                    })


        return {
            'email': user.email if user.email else None,
            'token': user.token,
            'phonenumber':user.phonenumber,
            'username': user.username,
            'is_active': employee_obj.is_active
        }
    


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('fullname', 'email', 'username', 'gender', 'phonenumber')



class CreateUserPermissionSerializer(serializers.ModelSerializer):

    def create_userPermission(self, validated_data):
        permission_name = validated_data.get('permission_name')
        permission_desc = validated_data.get('permission_desc')

        permission_obj = UserPermission.objects.create(permission_name= permission_name, permission_desc= permission_desc)


        return {
                'message':'Permission added successfully !!'
            }    



class UserPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPermission
        fields = '__all__'
