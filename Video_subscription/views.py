from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from .serializers import SignUpSerializer
# from .serializers import ChangePasswordSerializer
# from .serializers import UpdateProfileSerializer
# from .serializers import AdminChangePasswordSerializer
# from .serializers import AdminUpdateProfileSerializer
# from drf_yasg.utils import swagger_auto_schema
# from .openapi import change_password_responses
# from .openapi import CustomAutoSchema



class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (
        AllowAny,
    )
    serializer_class = SignUpSerializer

# Create your views here.
