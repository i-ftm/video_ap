"""
URL configuration for video_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from Video_subscription.views import SignUpView
from Video_subscription.views import ChangePasswordView
from Video_subscription.views import UpdateProfileView
from Video_subscription.views import AdminUpdateProfileView
from Video_subscription.views import AdminChangePasswordView
from Video_subscription.views import VideoViewSet
from Video_subscription.views import SubscriptionViewSet
from Video_subscription.views import HistoryViewSet


router = DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'history', HistoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/SignUp/' , SignUpView.as_view() , name= 'SignUp_auth'),
    path('api/change_password/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('api/update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('api/admin/change_password/<int:pk>/', AdminChangePasswordView.as_view(), name='auth_admin_change_password'),
    path('api/admin/update_profile/<int:pk>/', AdminUpdateProfileView.as_view(), name='admin_update_profile'),


]
