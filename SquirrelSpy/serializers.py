from rest_framework import serializers
from .models import Squirrel, User, Sighting

class SquirrelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squirrel
        fields = ['id', 'name', 'weight', 'sex', 'age', 'species', 'serial_num', 'left_ear_color', 'right_ear_color', 'image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_staff', 'is_active', 'date_joined', 'image']
        extra_kwargs = {'password': {'write_only': True}}

class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = ['id', 'user', 'squirrel', 'lat', 'long', 'time', 'behavior', 'certainty_level', 'is_verified', 'verification_comment', 'image']