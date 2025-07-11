# results/admin.py

from django.contrib import admin
from .models import ResultSection, ResultCard

@admin.register(ResultSection)
class ResultSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'updated_at')
    
    def has_add_permission(self, request):
        # Impede a criação de mais de uma instância de configuração.
        # Se já existir uma, o admin só poderá editá-la.
        return not ResultSection.objects.exists()

@admin.register(ResultCard)
class ResultCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'target_number', 'icon', 'order', 'is_active')
    list_editable = ('target_number', 'order', 'is_active')