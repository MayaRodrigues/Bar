from django.urls import path
from . import views

app_name = 'cardapio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('cardapio-comida/', views.cardapio_comida_view, name='cardapio_comida'),
    path('cardapio-jogos/', views.cardapio_jogos_view, name='cardapio_jogos'),
]
