# accounts/urls.py

from .views import SignUpView
from django.urls import path


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('login/', SignUpView.as_view(), name='signup'),
]

