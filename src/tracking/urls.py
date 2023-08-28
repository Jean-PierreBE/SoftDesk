from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracking.views import ProjectView, ContributorView, IssueView, CommentView

router = DefaultRouter()
router.register('projects', ProjectView, basename='project')
router.register('projects/(?P<project_id>[^/.]+)/users', ContributorView, basename='contributor')
router.register('projects/(?P<project_id>[^/.]+)/issues', IssueView, basename='issue')
router.register('projects/(?P<project_id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments', CommentView, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]
