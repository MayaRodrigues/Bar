from django.contrib import admin
from .models import Categoria, ItemCardapio, Jogo, CopiaJogo


# --- INLINE: Cópias de Jogo ---
class CopiaJogoInline(admin.TabularInline):
    """
    Permite editar cópias de jogos diretamente na página de edição do Jogo.
    Requisito: Utilização de formulários inline.
    """
    model = CopiaJogo
    extra = 1  # Mostra 1 linha vazia para adicionar nova cópia
    fields = ('identificador', 'disponivel', 'uso_atual')
    list_display = ('identificador', 'disponivel', 'uso_atual')


# --- ADMIN: Categoria ---
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Customização da lista de Categorias no Django Admin.
    Requisito: Customização/personalização da lista de objetos dos modelos.
    """
    list_display = ('nome', 'slug', 'icone')
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}  # Auto-gera slug a partir do nome
    list_filter = ('nome',)


# --- ADMIN: Item Cardápio ---
@admin.register(ItemCardapio)
class ItemCardapioAdmin(admin.ModelAdmin):
    """
    Customização da lista de Itens do Cardápio no Django Admin.
    Requisito: Customização/personalização da lista de objetos dos modelos.
    """
    list_display = ('nome', 'categoria', 'descricao_resumida')
    list_filter = ('categoria',)
    search_fields = ('nome', 'descricao')
    ordering = ('categoria', 'nome')
    
    def descricao_resumida(self, obj):
        """Mostra apenas os primeiros 50 caracteres da descrição"""
        return obj.descricao[:50] + '...' if len(obj.descricao) > 50 else obj.descricao
    descricao_resumida.short_description = 'Descrição'


# --- ADMIN: Jogo ---
@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    """
    Customização da lista de Jogos no Django Admin.
    Requisito: Customização/personalização da lista de objetos dos modelos.
    Requisito: Utilização de formulários inline (CopiaJogoInline).
    """
    list_display = ('nome', 'tipo', 'categoria', 'total_copias', 'copias_disponiveis_admin')
    list_filter = ('categoria', 'tipo')
    search_fields = ('nome', 'tipo', 'descricao')
    ordering = ('categoria', 'nome')
    
    # Adiciona o inline de cópias de jogos
    inlines = [CopiaJogoInline]
    
    def total_copias(self, obj):
        """Mostra o total de cópias cadastradas para este jogo"""
        return obj.copias.count()
    total_copias.short_description = 'Total de Cópias'
    
    def copias_disponiveis_admin(self, obj):
        """Mostra quantas cópias estão disponíveis no momento"""
        return obj.copias_disponiveis()
    copias_disponiveis_admin.short_description = 'Cópias Disponíveis'


# --- ADMIN: Cópia de Jogo ---
@admin.register(CopiaJogo)
class CopiaJogoAdmin(admin.ModelAdmin):
    """
    Customização da lista de Cópias de Jogos no Django Admin.
    Requisito: Customização/personalização da lista de objetos dos modelos.
    Permite aos funcionários registrar quais jogos estão sendo utilizados.
    """
    list_display = ('jogo', 'identificador', 'disponivel', 'uso_atual', 'status_colorido')
    list_filter = ('disponivel', 'jogo__categoria')
    search_fields = ('jogo__nome', 'identificador', 'uso_atual')
    list_editable = ('disponivel', 'uso_atual')  # Permite edição rápida na lista
    ordering = ('jogo__nome', 'identificador')
    
    def status_colorido(self, obj):
        """Mostra o status com cor para facilitar visualização"""
        if obj.disponivel:
            return '✅ Disponível'
        else:
            return f'🔴 Em Uso ({obj.uso_atual or "Não especificado"})'
    status_colorido.short_description = 'Status'


# Customização do título do Admin
admin.site.site_header = "Luna & Hops Tavern - Administração"
admin.site.site_title = "Admin Luna & Hops"
admin.site.index_title = "Gerenciamento do Bar de Jogos"
