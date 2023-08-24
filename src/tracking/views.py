# Create your views here.
from tracking.models import Project, Contributor, Issue, Comment
from tracking.serializers import ContributorSerializer, ProjectSerializer, \
    ProjectDetailSerializer, IssueSerializer, CommentSerializer
from tracking.permissions import UpdateOwnObjects, CreateComment, CreateIssue
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


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
        serializer.save(project_id=self.kwargs["project_id"], author_user=self.request.user)


class IssueView(viewsets.ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, UpdateOwnObjects, CreateIssue]

    def get_queryset(self):
        owncontributor_id = Contributor.objects.filter(author_user=self.request.user).values_list('project_id')
        queryset = Issue.objects.filter(Q(project_id__in=owncontributor_id) & Q(project_id__in=owncontributor_id))
        return queryset.filter(project_id=self.kwargs["project_id"])

    def perform_create(self, serializer):
        serializer.save(project_id=self.kwargs["project_id"], author_user=self.request.user)


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, UpdateOwnObjects, CreateComment]

    def get_queryset(self):
        owncontributor_id = Contributor.objects.filter(author_user=self.request.user).values_list('project_id')
        ownissue_id = Issue.objects.filter(Q(project_id__in=owncontributor_id) &
                                           Q(author_user=self.request.user)).values_list('id')
        queryset = Comment.objects.filter(issue_id__in=ownissue_id)
        return queryset.filter(issue_id=self.kwargs["issue_id"])

    def perform_create(self, serializer):
        serializer.save(issue_id=self.kwargs["issue_id"], author_user=self.request.user)
