from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracking.views import ProjectCreateView, ProjectUserView

router = DefaultRouter()
router.register('projects', ProjectUserView)

urlpatterns = [
    path('CreateProject/', ProjectCreateView.as_view()),
    path('', include(router.urls))
]