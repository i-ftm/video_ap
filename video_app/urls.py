from django.contrib import admin
from django.urls import include
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
from Video_subscription.viewset import VideoViewSet
from Video_subscription.viewset import SubscriptionViewSet
from Video_subscription.viewset import HistoryViewSet


router = DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'history', HistoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
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
