from django.db import models

from common.models import CommonFieldsModel




class Department(CommonFieldsModel):
    '''
        Model stores Department related information
    '''
    name = models.CharField(max_length=20, null=True, blank=True)
    
    class Meta:
        db_table = "department"



class Team(CommonFieldsModel):
    '''
        Model stores Team related information
    '''
    name = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    contact_info = models.CharField(null=True, blank=True, max_length=15)
    # shift = models.CharField(null=True, blank=True, max_length=15)
    
    class Meta:
        db_table = "team"