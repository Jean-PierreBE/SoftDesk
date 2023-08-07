from django.urls import path, include
from tracking.views import ProjectCreateView

urlpatterns = [
    path('Create Project/', ProjectCreateView.as_view())
]