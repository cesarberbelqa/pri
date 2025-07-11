# newsletter/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib import messages
from .forms import SubscriptionForm
from .models import Subscriber, EmailTemplate

class SubscribeView(CreateView):
    model = Subscriber
    form_class = SubscriptionForm
    template_name = 'newsletter/subscription_form.html' # Usaremos um formulário no rodapé, mas esta página pode existir
    success_url = reverse_lazy('newsletter:success')

    def form_valid(self, form):
        # Evitar erro se o e-mail já existir
        if Subscriber.objects.filter(email=form.cleaned_data['email']).exists():
            messages.warning(self.request, "Este e-mail já está cadastrado em nossa newsletter!")
            return self.form_invalid(form)

        response = super().form_valid(form)
        
        # Enviar e-mail de boas-vindas
        try:
            welcome_template = EmailTemplate.objects.get(is_welcome_template=True)
            subscriber = self.object
            
            template = Template(welcome_template.body)
            context = Context({'name': subscriber.name})
            html_body = template.render(context)
            
            send_mail(
                subject=welcome_template.subject,
                message='', # Django requer uma mensagem de texto, pode ser vazia
                from_email=None, # Usa DEFAULT_FROM_EMAIL de settings.py
                recipient_list=[subscriber.email],
                html_message=html_body,
                fail_silently=False
            )
            messages.success(self.request, "Inscrição realizada! Enviamos um e-mail de boas-vindas para você.")
        except EmailTemplate.DoesNotExist:
            messages.info(self.request, "Inscrição realizada com sucesso!")
        except Exception as e:
            messages.error(self.request, f"Ocorreu um erro ao enviar o e-mail de boas-vindas: {e}")

        return response

class SubscriptionSuccessView(TemplateView):
    template_name = 'newsletter/subscription_success.html'