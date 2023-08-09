from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from tracking.models import Project, Contributor, Issue
from tracking.serializers import ContributorSerializer, ProjectSerializer, ProjectDetailSerializer, IssueSerializer
from tracking.permissions import UpdateOwnObjects
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    contributor = Contributor()
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        else:
            return ProjectSerializer

    def perform_create(self, serializer):

        project = serializer.save()

        self.contributor.user = self.request.user
        self.contributor.role = "CRT"
        self.contributor.project_id = project.id
        self.contributor.save()

class ContributorView(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, UpdateOwnObjects]

class IssueView(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, UpdateOwnObjects]
