from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle

from .serializers import VideoSerializer
from .serializers import SubscriptionSerializer
from .serializers import HistorySerializer
from .models import Video
from .models import Subscription
from .models import History


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
