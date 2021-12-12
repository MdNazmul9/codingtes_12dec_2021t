from django.urls import path
from .views import SignupPageView, logout_view

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
]