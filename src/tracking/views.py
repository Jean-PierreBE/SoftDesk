from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from tracking.models import Project, Contributor, Issue, Comment
from tracking.serializers import ContributorSerializer, ProjectSerializer, \
    ProjectDetailSerializer, IssueSerializer, CommentSerializer
from tracking.permissions import UpdateOwnObjects
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        allcontributor = Contributor.objects.all()
        owncontributor_id = allcontributor.filter(author_user=self.request.user).values_list('project_id')
        return Project.objects.filter(id__in=owncontributor_id)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        else:
            return ProjectSerializer

    def perform_create(self, serializer):

        project = serializer.save()
        contributor = Contributor()
        contributor.author_user = self.request.user
        contributor.role = "CRT"
        contributor.project_id = project.id
        contributor.save()

class ContributorView(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, UpdateOwnObjects]

    def get_queryset(self):

        return self.queryset.filter(project_id=self.kwargs["project_id"])

    def perform_create(self, serializer):
        serializer.save(project_id=self.kwargs["project_id"],author_user=self.request.user)

class IssueView(viewsets.ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, UpdateOwnObjects]

    def get_queryset(self):
        owncontributor_id = Contributor.objects.filter(author_user=self.request.user).values_list('project_id')
        queryset = Issue.objects.filter(id__in=owncontributor_id)
        return queryset.filter(project_id=self.kwargs["project_id"])

    def perform_create(self, serializer):
        serializer.save(project_id=self.kwargs["project_id"],author_user=self.request.user)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, UpdateOwnObjects]

    def get_queryset(self):
        return self.queryset.filter(issue_id=self.kwargs["issue_id"])

    def perform_create(self, serializer):
        serializer.save(issue_id=self.kwargs["issue_id"],author_user=self.request.user)