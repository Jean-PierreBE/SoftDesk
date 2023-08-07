from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from tracking.models import Project, Contributor
from tracking.serializers import ContributorSerializer, ProjectSerializer

class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    contributor = Contributor()
    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):

        project = serializer.save()

        self.contributor.user = self.request.user
        self.contributor.role = "CRT"
        self.contributor.project_id = project.id
        self.contributor.save()


