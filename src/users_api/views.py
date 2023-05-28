from rest_framework import viewsets, filters

from users_api import serializers
from users_api import models
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('pseudo', 'first_name', 'last_name', 'email',)