from django.db import models

class LeadEconomia(models.Model):
    INTERESSE_CHOICES = [
        ('1', 'Nada'),
        ('2', 'Pouco'),
        ('3', 'Um pouco'),
        ('4', 'Interessado'),
        ('5', 'Muito interessado'),
    ]

    interesse = models.CharField(max_length=1, choices=INTERESSE_CHOICES, default='3', verbose_name="O quão interessado está?")
    quantidade_marmitas = models.IntegerField(verbose_name="Quantas marmitas por semana?")
    nome_completo = models.CharField(max_length=150, verbose_name="Como é seu nome?")
    whatsapp = models.CharField(max_length=20, verbose_name="Informe seu WhatsApp")
    marmitas_consumidas = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_completo} - {self.whatsapp}"