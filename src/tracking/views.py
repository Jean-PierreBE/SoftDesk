from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from tracking import serializers, models

class ProjectCreateView(generics.CreateAPIView):
    """
    Create a new ModelA entry with ModelB entry
    """
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectCreateSerializer
