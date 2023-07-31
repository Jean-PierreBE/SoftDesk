from django.urls import path, include

from tracking import views

urlpatterns = [
    path('projects/', views.ProjectCreateView.as_view())
]