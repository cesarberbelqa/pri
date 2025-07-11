from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import TestimonialForm
from .models import Testimonial

class TestimonialCreateView(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'testimonials/testimonial_form.html'
    success_url = reverse_lazy('testimonials:success')

    def form_valid(self, form):
        # Passa o valor do checkbox para a instância do modelo antes de salvar
        # Isso o torna acessível no sinal
        form.instance.subscribe_to_newsletter = form.cleaned_data.get('subscribe_to_newsletter')
        return super().form_valid(form)

class TestimonialSuccessView(TemplateView):
    """Displays a thank you page after a successful submission."""
    template_name = 'testimonials/testimonial_success.html'