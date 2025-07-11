# newsletter/admin.py

from django.contrib import admin, messages
from django.template import Template, Context
from django.core.mail import send_mass_mail
from django.utils import timezone
from .models import Subscriber, EmailTemplate, Campaign

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'created_at')
    search_fields = ('email', 'name')
    list_filter = ('is_active',)

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'is_welcome_template')
    list_filter = ('is_welcome_template',)

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'template', 'status', 'sent_at')
    list_filter = ('status', 'template')
    readonly_fields = ('sent_at', 'status')
    actions = ['send_campaign']

    @admin.action(description="Enviar campanha selecionada para todos os assinantes ativos")
    def send_campaign(self, request, queryset):
        for campaign in queryset:
            if campaign.status == 'SENT':
                messages.error(request, f"A campanha '{campaign.name}' já foi enviada.")
                continue

            subscribers = Subscriber.objects.filter(is_active=True)
            if not subscribers.exists():
                messages.warning(request, "Não há assinantes ativos para enviar a campanha.")
                continue

            template = Template(campaign.template.body)
            subject = campaign.template.subject
            
            # Usar send_mass_mail é muito mais eficiente
            datatuple = []
            for subscriber in subscribers:
                context = Context({'name': subscriber.name})
                html_body = template.render(context)
                message = (subject, '', None, [subscriber.email]) # plain text body is empty
                message_with_html = message[:2] + (html_body,) + message[3:]
                datatuple.append(message_with_html)

            send_mass_mail(datatuple, fail_silently=False)

            campaign.status = Campaign.StatusChoices.SENT
            campaign.sent_at = timezone.now()
            campaign.save()
            messages.success(request, f"Campanha '{campaign.name}' enviada para {subscribers.count()} assinantes.")