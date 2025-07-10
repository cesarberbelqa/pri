from django.urls import path
from .views import TestimonialCreateView, TestimonialSuccessView

app_name = 'testimonials'

urlpatterns = [
    # URL for submitting a new testimonial (e.g., /depoimentos/deixar-depoimento/)
    path('submit/', TestimonialCreateView.as_view(), name='create'),

    # URL for the "thank you" page after submission
    path('success/', TestimonialSuccessView.as_view(), name='success'),
]