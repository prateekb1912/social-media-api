from django.urls import path
from .views import AuthenticateView

urlpatterns = [
    path('authenticate', AuthenticateView.as_view(), name='authenticate'),
]