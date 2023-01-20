from rest_framework import serializers
from django.contrib.auth.models import User
from .models import HotelUser

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


# class RoomTypesSerializer(serializers.ModelSerializer):
#     admin = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     class Meta:
#         model = RoomTypes
#         fields =  ['id', 'room_type', 'admin']


# class BinaryField(serializers.Field):
#     def to_representation(self, value):
#         return value.decode('utf-8')

#     def to_internal_value(self, value):
#          return value.encode('utf-8')

class HotelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelUser
        fields=('username','image')
        
    # image = BinaryField()