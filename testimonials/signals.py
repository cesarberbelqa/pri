# testimonials/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Template, Context
from django.core.mail import send_mail
from .models import Testimonial
from newsletter.models import Subscriber, EmailTemplate

@receiver(post_save, sender=Testimonial)
def add_testimonial_author_to_newsletter(sender, instance, created, **kwargs):
    """
    Quando um novo depoimento é criado, adiciona o autor à lista de assinantes
    e envia o e-mail de boas-vindas, se ele ainda não for um assinante.
    """
    # Acessa o valor do campo do formulário que não foi salvo no modelo
    subscribe = getattr(instance, 'subscribe_to_newsletter', False)
    
    # Executa apenas para novos depoimentos e se o usuário consentiu
    if created and subscribe:
        # get_or_create retorna o objeto e um booleano (True se foi criado, False se já existia)
        subscriber, was_created = Subscriber.objects.get_or_create(
            email=instance.email,
            defaults={'name': instance.name}
        )

        # Envia e-mail de boas-vindas apenas se for um assinante totalmente novo
        if was_created:
            try:
                welcome_template = EmailTemplate.objects.get(is_welcome_template=True)
                template = Template(welcome_template.body)
                context = Context({'name': subscriber.name})
                html_body = template.render(context)
                
                send_mail(
                    subject=welcome_template.subject,
                    message='',
                    from_email=None,
                    recipient_list=[subscriber.email],
                    html_message=html_body,
                )
            except EmailTemplate.DoesNotExist:
                # Se não houver template de boas-vindas, não faz nada.
                pass 