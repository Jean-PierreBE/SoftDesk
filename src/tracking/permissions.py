from rest_framework import permissions


class UpdateOwnObjects(permissions.BasePermission):
    """Allow user to edit their own objects"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own objects"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author_user.id == request.user.id
