from django.shortcuts import render, redirect
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