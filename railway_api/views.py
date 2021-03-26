from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from railway_api import serializers, models
from railway_api.serializers import AuthUserRegistrationSerializer, AuthUserLoginSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = IsAuthenticated,
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.UserProfileSerializer(queryset, many=True)
        return GenericResponses.make_generic_response(self,serializer.data,True,'')

class RailwayPassengerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RailwayPassengerSerializer
    queryset = models.RailwayPassenger.objects.all()
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.RailwayPassengerSerializer(queryset, many=True)
        return GenericResponses.make_generic_response(self, serializer.data, True, '')


class GenericResponses:
    def make_generic_response(self,data,isSuccess,message=''):
        resp_data = {'isSuccess': isSuccess,'message':message, 'data': data}
        return Response(resp_data)


class AuthUserRegistrationView(APIView):
    serializer_class = AuthUserRegistrationSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            response = {
                'email': serializer.data['email'],
                'mobile':serializer.data['mobile']
            }
            return GenericResponses.make_generic_response(self,response,True,'User registration is successful')

class AuthUserLoginView(APIView):
    serializer_class = AuthUserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            response = {
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }
            return GenericResponses.make_generic_response(self,response,True,'User logged in successfully')