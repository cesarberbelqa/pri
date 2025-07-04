from django.contrib.auth.views import LoginView, LogoutView
from .forms import EmailAuthenticationForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

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

@login_required
def home(request):
    return render(request, 'accounts/home.html')