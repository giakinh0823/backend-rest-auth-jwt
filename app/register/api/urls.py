from rest_framework import routers
from .views import UserViewSet, RegisterViewSet, ProfileViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("profile", ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterViewSet.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
