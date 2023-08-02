from django.db import models

from common.models import CommonFieldsModel




class Shift(CommonFieldsModel):
    '''
        Model stores Shift related information
    '''
    name = models.CharField(max_length=15, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    duration_in_hrs = models.FloatField(null=True, blank=True)
    min_staff_required = models.IntegerField(blank=True, null=True)
    max_staff_allowed = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = "shift"
