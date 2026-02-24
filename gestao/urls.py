from django.urls import path
from . import views

urlpatterns = [
    path('', views.economia_view, name='economia'),
    path('sucesso/', views.sucesso_view, name='pagina_sucesso'),
    path('negociacao/', views.negociacao_view, name='pagina_negociacao'),
    path('convenios/', views.convenios_view, name='pagina_convenios'),
    path('registrar-consumo/<int:lead_id>/', views.registrar_consumo, name='registrar_consumo'),
path('excluir-convenio/<int:lead_id>/', views.excluir_convenio, name='excluir_convenio'),
]