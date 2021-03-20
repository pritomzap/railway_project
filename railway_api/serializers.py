from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','name','email','age','gender','state','city','mobile')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
