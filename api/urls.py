from django.urls import path
from .views import AuthenticateView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('authenticate', AuthenticateView.as_view(), name='authenticate'),
    path('follow/<int:id>', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:id>', UnfollowUserView.as_view(), name='unfollow_user'),
]