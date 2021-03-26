from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','email','first_name','last_name','age','gender','state','city','mobile')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

class RailwayPassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RailwayPassenger
        fields = ('pnr','user','user_id','route_id','train_id','seat_amount')


class AuthUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','email','password','first_name','last_name','age','gender','state','city','mobile')

    def create(self, validated_data):
        auth_user = UserProfile.objects.create_user(**validated_data)
        return auth_user

class AuthUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("No user exist with this email")
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        update_last_login(None, user)

        validation = {
            'access': access_token,
            'refresh': refresh_token,
            'email': user.email,
            'full_name': user.get_name(),
            'role': user.role,
        }
        return validation