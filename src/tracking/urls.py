from django.urls import path, include
from tracking.views import ProjectCreateView

urlpatterns = [
    path('projects/', ProjectCreateView.as_view())
]