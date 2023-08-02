from django.db import models
from common.constants import Choices
from common.models import CommonFieldsModel
from team.models import Team
from user.models import User, UserRole
import random
import uuid




marital_status = (
    ('married', 'Married'),
    ('unmarried', 'Unmarried'),
    ('divorced', 'Divorced'),
)


def create_empolyee_code():
    return str(random.randint(1000000000, 9999999999))


def image_upload_to(instance, filename):
    uid = str(uuid.uuid4())
    ext = filename.split(".")[-1].lower()
    return "employee/profile-images/{}/{}.{}".format(instance.pk, uid, ext)



class EmployeeProfile(CommonFieldsModel):
    '''
        Model stores employee related information
    '''
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name="employee_profile")
    user_group = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True, blank=True, related_name="user_group")
    father_name = models.CharField(max_length=100, null=True, blank=True)
    marital_status = models.CharField(max_length=10, choices=marital_status, default='unmarried', null=True, blank=True)
    image = models.ImageField(upload_to=image_upload_to, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    shareReferralCode = models.CharField(max_length=20, blank=True, null=True, help_text="User's own referral code")
    usedReferralCode = models.CharField(max_length=20, blank=True, null=True, help_text="code used while registration")
    reporting_person = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="reporting_person")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    is_team_lead = models.BooleanField(default=False)
    active_inactive_date = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = "employee_profile"



class FamilyProfile(CommonFieldsModel):
    '''
        Model stores family related information
    '''
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(null=True, blank=True, max_length=50)
    phonenumber = models.CharField(null=True, blank=True, max_length=15)
    gender = models.CharField(max_length=10, choices=Choices.gender_choices)
    image = models.ImageField(upload_to=image_upload_to, null=True, blank=True)
    relationship = models.CharField(max_length=20, null=True, blank=True)
    is_emergency_contact = models.BooleanField(default=False)
    age_in_yrs = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = "family_profile"