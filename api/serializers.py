from rest_framework import serializers
from .models import Student, Building, Room, Key

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('__all__')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('__all__')


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ('__all__')
