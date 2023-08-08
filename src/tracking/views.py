from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from tracking.models import Project, Contributor
from tracking.serializers import ContributorSerializer, ProjectSerializer
from tracking.permissions import UpdateOwnObjects
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    contributor = Contributor()
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):

        project = serializer.save()

        self.contributor.user = self.request.user
        self.contributor.role = "CRT"
        self.contributor.project_id = project.id
        self.contributor.save()

class ProjectUserView(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


