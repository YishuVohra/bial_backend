from datetime import datetime
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer
from employee.models import EmployeeProfile
from user.models import UserRole




class FetchAllAttendancesAPIView(ListAPIView):
	serializer_class = AttendanceSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		request_user = self.request.user
		employee_profile_obj = EmployeeProfile.objects.get(user = request_user)

		if employee_profile_obj:
			role_obj = UserRole.objects.get(id=employee_profile_obj.user_group.id)

		if role_obj and role_obj.role_name == "admin":
			employee_list_obj = EmployeeProfile.objects.filter(is_active = True)
			destructureArray = []

		else:
			employee_list_obj = EmployeeProfile.objects.filter(reporting_person = request_user, is_active = True)
			destructureArray = []
			destructureArray.append(employee_profile_obj)

		for employee in employee_list_obj:
			destructureArray.append(employee)

		current_date = datetime.today()

		result = []
		for employee_obj in destructureArray:
			attendance, _ = Attendance.objects.get_or_create(employee = employee_obj, attendance_date = current_date)

			queryset = Attendance.objects.filter(id = attendance.id)
			result += queryset

		return result



class UpdateAttendanceAPIView(UpdateAPIView):
	permission_classes = (IsAuthenticated,)

	def put(self, request, *args, **kwargs):
		attendance_id = request.data.get('attendance_id')
		attendance_obj = Attendance.objects.filter(id = attendance_id).last()

		current_time = datetime.today()

		if request.data.get('attendance'):
			attendance_obj.attendance = request.data['attendance']
		if request.data.get('first_half'):
			attendance_obj.first_half = request.data['first_half']
		if request.data.get('second_half'):
			attendance_obj.second_half = request.data['second_half']

		if attendance_obj.attendance == "present" or attendance_obj.attendance == "Present":
			attendance_obj.attendance_time = current_time

		attendance_obj.is_attendance_done = True
		attendance_obj.save()

		return Response({"message": "Updated Attendance successfully"}, status=201)


