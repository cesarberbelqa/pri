from django.urls import path
from .views import SubscribeView, SubscriptionSuccessView

app_name = 'newsletter'

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('success/', SubscriptionSuccessView.as_view(), name='success'),
]