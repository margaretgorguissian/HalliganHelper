import logging

from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework_nested.relations import NestedHyperlinkedRelatedField

from ..models import (School, Course, CustomUser,
                      Student, Request, OfficeHour)

from ..utils import get_administrators_for_school

logger = logging.getLogger(__name__)


class SimpleCourseSerializer(serializers.ModelSerializer):
    identifier = serializers.CharField(source='get_identifier')

    class Meta:
        model = Course
        fields = ('id', 'name', 'identifier',)


class RequestorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    headshot_url = serializers.ImageField(source='headshot',
                                          read_only=True)

    class Meta:
        model = Student
        fields = ('headshot_url', 'first_name', 'last_name',)


class CourseSerializer(serializers.ModelSerializer):
    identifier = serializers.CharField(source='get_identifier')

    class Meta:
        model = Course
        fields = ('id', 'name', 'identifier',)


class OfficeHourSerializer(serializers.ModelSerializer):
    ta = RequestorSerializer(read_only=True)

    class Meta:
        model = OfficeHour
        fields = ('id', 'location', 'start_time', 'end_time', 'ta',)


class RequestSerializer(serializers.ModelSerializer):
    requestor = RequestorSerializer(read_only=True)

    class Meta:
        model = Request
        fields = ('id', 'question', 'where_located', 'cancelled',
                  'checked_out', 'solved', 'requestor', 'expired')


class SchoolAdminSerializer(serializers.ModelSerializer):
    headshot_url = serializers.ImageField(source='student.headshot',
                                          read_only=True)
    full_name = serializers.CharField(source='get_full_name',
                                      read_only=True)
    is_head_admin = serializers.SerializerMethodField()

    def get_is_head_admin(self, user):
        return hasattr(user, 'school')

    class Meta:
        model = CustomUser
        fields = ('email', 'headshot_url', 'is_head_admin', 'full_name')


class SchoolSerializer(serializers.ModelSerializer):
    courses = SimpleCourseSerializer(many=True, read_only=True)
    administrators = serializers.SerializerMethodField()

    def get_administrators(self, school):
        admins = get_administrators_for_school(school)
        return SchoolAdminSerializer(admins, many=True).data

    class Meta:
        model = School
        fields = ('name', 'administrators', 'courses',)