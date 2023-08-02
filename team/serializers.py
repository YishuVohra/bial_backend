from rest_framework import serializers
from rest_framework.exceptions import ParseError, NotFound, ValidationError, NotAcceptable

from team.models import Department, Team





class CreateTeamSerializer(serializers.ModelSerializer):

    def create_team(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        department = validated_data.get('department_id')
        contact_info = validated_data.get('contact_info')

        department_obj = Department.objects.filter(id = department).last()

        team_obj = Team.objects.create(name= name, description= description, department= department_obj, contact_info= contact_info)


        return {
                'message':'Team details added successfully !!'
            }
    


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'
    


class TeamSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = '__all__'

    def get_department(self, instance):
        try:
            department = DepartmentSerializer(instance.department).data
        except:
            department = None
        return department

