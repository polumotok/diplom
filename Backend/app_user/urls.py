from django.urls import path

from .views import ProfileView, Avatar, PasswordView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("profile/avatar", Avatar.as_view(), name="avatar"),
    path("profile/password", PasswordView.as_view(), name="avatar"),
]
