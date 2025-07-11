from django.contrib.auth.views import LoginView, LogoutView
from .forms import EmailAuthenticationForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from services.models import Service        # Importe o modelo Service
from testimonials.models import Testimonial
from results.models import ResultSection, ResultCard 

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
    # Busca os 6 primeiros serviços ativos, respeitando a ordenação definida no admin
    featured_services = Service.objects.filter(ativo=True)[:6]

    # 2. Fetch 5 random, approved, and active testimonials
    random_testimonials = Testimonial.objects.filter(
        status=Testimonial.StatusChoices.APPROVED, 
        is_active=True
    ).order_by('?').values('name', 'body')[:3] # Using .values() for efficiency

    result_section = ResultSection.objects.filter(is_active=True).first()
    result_cards = ResultCard.objects.filter(is_active=True).order_by('order')[:4] # Limita a 4 cards

    # 3. Pass them to the template context
    context = {
        'services': featured_services,
        'testimonials': random_testimonials,
        'result_section': result_section, # 3. Passe para o contexto
        'result_cards': result_cards,     
    }
    
    return render(request, 'accounts/home.html', context) # Assumes your template is 'home.html'