from django.shortcuts import render

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, HotelUserSerializer


from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import HotelUser
from rest_framework.views import APIView
from rest_framework import generics

from django.contrib.auth import get_user_model

User = get_user_model()

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


@api_view(['GET'])
def getHotelUser(request):
    h_user = HotelUser.objects.all()
    serializer = HotelUserSerializer(h_user, many=True)
    return Response(serializer.data)

        

# class getHotelUser(generics.ListAPIView):
#     queryset = HotelUser.objects.all()
#     serializer_class = HotelUserSerializer

    
@api_view(['POST'])
def postHotelUser(request):
    serializer = HotelUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)