from rest_framework import permissions
from tracking.models import Project, Contributor
from django.db.models import Q
from django.shortcuts import get_object_or_404


class UpdateOwnObjects(permissions.BasePermission):
    """Allow user to edit their own objects"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own objects"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author_user.id == request.user.id


class CreateIssueComment(permissions.BasePermission):
    """Allow user to edit their own objects"""

    def has_permission(self, request, view):
        parent_project = get_object_or_404(Project, pk=view.kwargs['project_id'])
        user_project = Contributor.objects.filter(Q(project_id=parent_project.id) &
                                                  Q(author_user=request.user))
        if user_project.exists():
            return True
        else:
            return False
