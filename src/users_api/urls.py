from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users_api import views


router = DefaultRouter()
router.register('signup', views.UserProfileViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
