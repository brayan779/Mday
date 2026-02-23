from django.contrib import admin
from .models import LeadEconomia

@admin.register(LeadEconomia)
class LeadEconomiaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'whatsapp', 'quantidade_marmitas', 'data_criacao')
    search_fields = ('nome_completo', 'whatsapp')