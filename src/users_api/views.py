from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from users_api import serializers, models, permissions, paginations

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    pagination_class = paginations.UserListPagination
    queryset = models.UserProfile.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('pseudo', 'first_name', 'last_name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
