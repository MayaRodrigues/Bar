import json
import os
from django.core.management.base import BaseCommand
from django.core.files import File
from cardapio.models import Categoria, ItemCardapio, Jogo, CopiaJogo
from pathlib import Path


class Command(BaseCommand):
    help = 'Popula o banco de dados com dados dos arquivos JSON'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando população do banco de dados...'))
        
        # Limpa dados existentes (opcional - comente se não quiser limpar)
        self.stdout.write('Limpando dados existentes...')
        CopiaJogo.objects.all().delete()
        Jogo.objects.all().delete()
        ItemCardapio.objects.all().delete()
        Categoria.objects.all().delete()
        
        # Cria categorias
        self.stdout.write('Criando categorias...')
        categorias = {
            'comidas': Categoria.objects.create(nome='Comidas', slug='comidas', icone='🍽️'),
            'bebidas': Categoria.objects.create(nome='Bebidas', slug='bebidas', icone='🍹'),
            'sobremesas': Categoria.objects.create(nome='Sobremesas', slug='sobremesas', icone='🍰'),
            'pocoes-especiais': Categoria.objects.create(nome='Poções Especiais', slug='pocoes-especiais', icone='🧪'),
            'tabuleiro': Categoria.objects.create(nome='Tabuleiro', slug='tabuleiro', icone='🎲'),
            'maquinas': Categoria.objects.create(nome='Máquinas', slug='maquinas', icone='🕹️'),
        }
        
        # Popula cardápio de comidas
        self.stdout.write('Populando cardápio de comidas...')
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        comidas_json = base_dir / 'data' / 'comidas.json'
        
        if comidas_json.exists():
            with open(comidas_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            cardapio = data.get('cardapio', {})
            
            # Processa comidas
            for item in cardapio.get('comidas', []):
                ItemCardapio.objects.create(
                    nome=item['nome'],
                    descricao=item['descricao'],
                    categoria=categorias['comidas'],
                    imagem=''  # Imagens serão adicionadas manualmente via admin
                )
                self.stdout.write(f'  - Criado: {item["nome"]}')
            
            # Processa bebidas
            for item in cardapio.get('bebidas', []):
                ItemCardapio.objects.create(
                    nome=item['nome'],
                    descricao=item['descricao'],
                    categoria=categorias['bebidas'],
                    imagem=''
                )
                self.stdout.write(f'  - Criado: {item["nome"]}')
            
            # Processa sobremesas
            for item in cardapio.get('sobremesas', []):
                ItemCardapio.objects.create(
                    nome=item['nome'],
                    descricao=item['descricao'],
                    categoria=categorias['sobremesas'],
                    imagem=''
                )
                self.stdout.write(f'  - Criado: {item["nome"]}')
        
        # Popula jogos
        self.stdout.write('Populando jogos...')
        jogos_json = base_dir / 'data' / 'jogos.json'
        
        if jogos_json.exists():
            with open(jogos_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            jogos_data = data.get('jogos', {})
            
            # Processa jogos de tabuleiro
            for item in jogos_data.get('tabuleiro', []):
                jogo = Jogo.objects.create(
                    nome=item['nome'],
                    tipo=item['tipo'],
                    descricao=item.get('descricao', ''),
                    categoria=categorias['tabuleiro'],
                    imagem=''
                )
                self.stdout.write(f'  - Criado: {item["nome"]}')
                
                # Cria 2 cópias de exemplo para cada jogo
                for i in range(1, 3):
                    CopiaJogo.objects.create(
                        jogo=jogo,
                        identificador=f'{jogo.nome[:3].upper()}-{i:03d}',
                        disponivel=True if i == 1 else False,
                        uso_atual=None if i == 1 else f'Mesa {i}'
                    )
                    self.stdout.write(f'    - Cópia criada: {jogo.nome[:3].upper()}-{i:03d}')
            
            # Processa máquinas arcade
            for item in jogos_data.get('maquinas', []):
                jogo = Jogo.objects.create(
                    nome=item['nome'],
                    tipo=item['tipo'],
                    descricao=item.get('descricao', ''),
                    categoria=categorias['maquinas'],
                    imagem=''
                )
                self.stdout.write(f'  - Criado: {item["nome"]}')
                
                # Cria 1 cópia para cada máquina (geralmente só há uma)
                CopiaJogo.objects.create(
                    jogo=jogo,
                    identificador=f'{jogo.nome[:3].upper()}-001',
                    disponivel=True,
                    uso_atual=None
                )
                self.stdout.write(f'    - Cópia criada: {jogo.nome[:3].upper()}-001')
        
        self.stdout.write(self.style.SUCCESS('\n✅ Banco de dados populado com sucesso!'))
        self.stdout.write(self.style.WARNING('\n⚠️  IMPORTANTE: As imagens devem ser adicionadas manualmente via Django Admin.'))
        self.stdout.write(self.style.WARNING('   Acesse /admin/ e faça upload das imagens para cada item.'))
