from django.urls import path
from .views import CustomLoginView, RegisterView, home
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
]
