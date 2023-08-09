from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracking.views import ProjectView, ContributorView, IssueView

router = DefaultRouter()
router.register('project', ProjectView, basename='project')
router.register('contributor', ContributorView, basename='contributor')
router.register('project/<pk>/issue', IssueView, basename='project-detail')

urlpatterns = [
    path('', include(router.urls))
]