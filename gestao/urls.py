from django.urls import path
from . import views

urlpatterns = [
    path('', views.economia_view, name='economia'),
    path('sucesso/', views.sucesso_view, name='pagina_sucesso'),
]