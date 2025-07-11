# newsletter/models.py

from django.db import models
from django.template import Template, Context
from django.core.mail import send_mail

class Subscriber(models.Model):
    """Armazena todos os contatos que optaram por receber e-mails."""
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Assinante"
        verbose_name_plural = "Assinantes"
        ordering = ['-created_at']

    def __str__(self):
        return self.email

class EmailTemplate(models.Model):
    """Templates de e-mail que podem ser criados no admin."""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome Interno do Template")
    subject = models.CharField(max_length=255, verbose_name="Assunto do E-mail")
    body = models.TextField(
        verbose_name="Corpo do E-mail (HTML)",
        help_text="Use {{ name }} para inserir o nome do assinante."
    )
    is_welcome_template = models.BooleanField(
        default=False, 
        verbose_name="É o template de Boas-Vindas?",
        help_text="Marque se este for o e-mail enviado automaticamente para novos assinantes."
    )

    class Meta:
        verbose_name = "Template de E-mail"
        verbose_name_plural = "Templates de E-mail"

    def __str__(self):
        return self.name

class Campaign(models.Model):
    """Campanhas para envio manual de e-mails."""
    class StatusChoices(models.TextChoices):
        DRAFT = 'DRAFT', 'Rascunho'
        SENT = 'SENT', 'Enviada'

    name = models.CharField(max_length=255, verbose_name="Nome da Campanha")
    template = models.ForeignKey(EmailTemplate, on_delete=models.PROTECT, verbose_name="Template")
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.DRAFT)
    sent_at = models.DateTimeField(null=True, blank=True, verbose_name="Enviada em")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Campanha Manual"
        verbose_name_plural = "Campanhas Manuais"

    def __str__(self):
        return self.name