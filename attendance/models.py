from django.db import models

from common.models import CommonFieldsModel
from employee.models import EmployeeProfile




attendance_status = (
	('present','Present'),
	('absent','Absent'),
	('pending','Pending')
)




class Attendance(CommonFieldsModel):
	'''
	Model stores BOD EOD tasks related information
	'''
	employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True, blank=True)
	attendance_date = models.DateField(null=True, blank=True)
	attendance_time = models.TimeField(null=True, blank=True)
	attendance = models.CharField(max_length=20, choices = attendance_status, blank=True, null=True, default='pending')
	first_half = models.BooleanField(default=False)
	second_half = models.BooleanField(default=False)
	is_attendance_done = models.BooleanField(default=False)

	class Meta:
	    db_table = "attendance"