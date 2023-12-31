
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserViewSet, UserSendMessage

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('message/', UserSendMessage.as_view(), name='user_message'),
    path('', include(router.urls)),
]
