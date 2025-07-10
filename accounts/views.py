from django.contrib.auth.views import LoginView, LogoutView
from .forms import EmailAuthenticationForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from testimonials.models import Testimonial

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Registro efetuado com sucesso! Bem-vindo(a).")
        return super().form_valid(form)


class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = 'accounts/login.html'

def home(request):

    # 2. Fetch 5 random, approved, and active testimonials
    random_testimonials = Testimonial.objects.filter(
        status=Testimonial.StatusChoices.APPROVED, 
        is_active=True
    ).order_by('?').values('name', 'body')[:5] # Using .values() for efficiency

    # 3. Pass them to the template context
    context = {
        'testimonials': random_testimonials,
        # ... other context variables for your home page
    }
    
    return render(request, 'accounts/home.html', context) # Assumes your template is 'home.html'