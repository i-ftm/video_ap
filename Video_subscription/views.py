from django.contrib.auth.models import User
from .models import Video
from .models import Subscription
from .models import History
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from rest_framework import viewsets
from .serializers import SignUpSerializer
from .serializers import ChangePasswordSerializer
from .serializers import UpdateProfileSerializer
from .serializers import AdminChangePasswordSerializer
from .serializers import AdminUpdateProfileSerializer
from .serializers import VideoSerializer
from .serializers import SubscriptionSerializer
from .serializers import HistorySerializer



class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (
        AllowAny,
    )
    serializer_class = SignUpSerializer
    

class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({'success': True})
    

class UpdateProfileView(generics.GenericAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = UpdateProfileSerializer
    throttle_classes = [
        AnonRateThrottle,
        UserRateThrottle,
    ]

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({'success': True})


class AdminChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (
        IsAdminUser,
    )
    serializer_class = AdminChangePasswordSerializer

class AdminUpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (
        IsAdminUser,
    )
    serializer_class = AdminUpdateProfileSerializer
    

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

# Create your views here.
