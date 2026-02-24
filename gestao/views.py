from django.shortcuts import render, redirect, get_object_or_404
from .models import LeadEconomia

def economia_view(request):
    if request.method == "POST":
        # Pegando os dados do formulário
        interesse = request.POST.get('interesse')
        quantidade = request.POST.get('quantidade')
        nome = request.POST.get('nome')
        whatsapp = request.POST.get('whatsapp')

        # Salvando no banco de dados
        LeadEconomia.objects.create(
            interesse=interesse,
            quantidade_marmitas=quantidade,
            nome_completo=nome,
            whatsapp=whatsapp
        )
        # Redireciona para a página de sucesso
        return redirect('pagina_sucesso')

    return render(request, 'gestao/economia.html')

def sucesso_view(request):
    return render(request, 'gestao/sucesso.html')

def negociacao_view(request):
    # Puxa todos os leads do banco para listar nos cards
    leads = LeadEconomia.objects.all().order_by('-data_criacao')
    return render(request, 'gestao/negociacao.html', {'leads': leads})

def convenios_view(request):
    # Aqui depois filtraremos apenas quem foi marcado como "Fechado"
    leads = LeadEconomia.objects.all()
    return render(request, 'gestao/convenios.html', {'leads': leads})

def registrar_consumo(request, lead_id):
    if request.method == "POST":
        lead = get_object_or_404(LeadEconomia, id=lead_id)
        lead.marmitas_consumidas += 1
        lead.save()
    return redirect('pagina_convenios')
def excluir_convenio(request, lead_id):
    lead = get_object_or_404(LeadEconomia, id=lead_id)
    lead.delete()
    return redirect('pagina_convenios')
