from django.shortcuts import render
from .models import Categoria, ItemCardapio, Jogo


def home_view(request):
    """
    View da página inicial.
    Renderiza o template index.html.
    """
    return render(request, 'cardapio/index.html')


def cardapio_comida_view(request):
    """
    View do cardápio de comidas, bebidas e sobremesas.
    Gera dinamicamente a partir dos dados do banco de dados.
    Requisito: Páginas geradas dinamicamente utilizando Django.
    """
    # Busca todas as categorias de cardápio (comidas, bebidas, sobremesas)
    categorias_cardapio = Categoria.objects.filter(
        slug__in=['comidas', 'bebidas', 'sobremesas', 'pocoes-especiais']
    ).prefetch_related('itens_cardapio')
    
    # Organiza os itens por categoria
    context = {
        'categorias': categorias_cardapio,
    }
    
    return render(request, 'cardapio/cardapio_comida.html', context)


def cardapio_jogos_view(request):
    """
    View do cardápio de jogos.
    Gera dinamicamente a partir dos dados do banco de dados.
    Requisito: Páginas geradas dinamicamente utilizando Django.
    Requisito: Informação de quantas cópias de cada jogo estão disponíveis.
    """
    # Busca todas as categorias de jogos (tabuleiro, máquinas)
    categorias_jogos = Categoria.objects.filter(
        slug__in=['tabuleiro', 'maquinas']
    ).prefetch_related('jogos__copias')
    
    # Busca todos os jogos com suas cópias
    jogos_tabuleiro = Jogo.objects.filter(
        categoria__slug='tabuleiro'
    ).prefetch_related('copias')
    
    jogos_maquinas = Jogo.objects.filter(
        categoria__slug='maquinas'
    ).prefetch_related('copias')
    
    context = {
        'categorias': categorias_jogos,
        'jogos_tabuleiro': jogos_tabuleiro,
        'jogos_maquinas': jogos_maquinas,
    }
    
    return render(request, 'cardapio/cardapio_jogos.html', context)