from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import TestimonialForm
from .models import Testimonial

class TestimonialCreateView(CreateView):
    """View to handle the creation of a new testimonial."""
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'testimonials/testimonial_form.html'
    success_url = reverse_lazy('testimonials:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Leave Your Testimonial'
        return context

class TestimonialSuccessView(TemplateView):
    """Displays a thank you page after a successful submission."""
    template_name = 'testimonials/testimonial_success.html'