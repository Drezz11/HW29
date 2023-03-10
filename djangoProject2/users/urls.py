from django.urls import path

from users.views import UserListView, UserDetailView, UserCreateView, UserDeleteView, UserUpdateView, LocationViewSet
from rest_framework import routers

urlpatterns = {
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
}

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns += router.urls