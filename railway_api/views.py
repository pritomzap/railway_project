from rest_framework import viewsets
from rest_framework.response import Response
from railway_api import serializers,models


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.UserProfileSerializer(queryset, many=True)
        return GenericResponses.make_generic_response(self,serializer.data,True,'')

class GenericResponses:
    def make_generic_response(self,data,isSuccess,message=''):
        resp_data = {'isSuccess': isSuccess,'message':message, 'data': data}
        return Response(resp_data)
