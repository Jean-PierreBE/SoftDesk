from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users_api import views


router = DefaultRouter()
router.register('signup', views.UserProfileViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
