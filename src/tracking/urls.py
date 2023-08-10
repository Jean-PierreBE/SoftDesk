from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracking.views import ProjectView, ContributorView, IssueView, CommentView

router = DefaultRouter()
router.register('project', ProjectView, basename='project')
router.register('contributor', ContributorView, basename='contributor')
router.register('project/(?P<project_id>[^/.]+)/issue', IssueView, basename='issue')
router.register('project/(?P<project_id>[^/.]+)/issue/(?P<issue_id>[^/.]+)/comment', CommentView, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]