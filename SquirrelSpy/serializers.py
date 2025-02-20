from rest_framework import serializers
from .models import Squirrel, User, Sighting

class SquirrelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squirrel
        fields = ['id', 'name', 'weight', 'sex', 'age', 'species', 'serial_num', 'left_ear_color', 'right_ear_color', 'image']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_staff', 'is_active', 'date_joined', 'image']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'image')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SightingSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Sighting
        fields = ['id', 'user', 'squirrel', 'lat', 'long', 'time', 'behavior', 'certainty_level', 'is_verified', 'verification_comment', 'comment', 'image']