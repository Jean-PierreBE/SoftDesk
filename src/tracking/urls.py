from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracking.views import ProjectView, ContributorView

router = DefaultRouter()
router.register('project', ProjectView,basename='project')
router.register('contributor', ContributorView,basename='contributor')

urlpatterns = [
    path('', include(router.urls))
]