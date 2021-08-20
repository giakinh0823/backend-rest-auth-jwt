from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from register.models import Profile
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.generic import ListView, DetailView



class RegisterViewSet(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh=None
        if user:
            profile = Profile.objects.create(user=user, phone_number=request.data.get(
                "phone_number"), address=request.data.get("address"))
            profile.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "username"]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "phone_number", "address", "slug"]
