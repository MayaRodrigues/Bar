import json
import os
from django.core.management.base import BaseCommand
from django.core.files import File
from cardapio.models import Categoria, ItemCardapio, Jogo, CopiaJogo
from pathlib import Path
import shutil


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
        
        # Caminhos base
        project_root = Path(__file__).resolve().parent.parent.parent.parent
        static_root = project_root / 'cardapio' / 'static'
        data_images_root = project_root / 'catalogo_pronto' / 'images'

        def image_path_from_json(json_path: str) -> Path:
            """
            Converte '/assets/images/..' do JSON para caminho real, priorizando 'data/images/...'
            e fazendo fallback para 'cardapio/static/images/...'.
            """
            # Normaliza e remove prefixo '/'
            rel = json_path.lstrip('/')
            # Substitui 'assets/' por '' porque as imagens estão em 'static/images/...'
            if rel.startswith('assets/'):
                rel = rel.replace('assets/', '', 1)
            # Para a pasta data/images usamos o caminho SEM o prefixo 'images/'
            # Ex.: 'images/jogos/...' -> 'jogos/...'
            rel_no_images_prefix = rel[7:] if rel.startswith('images/') else rel
            # Primeiro tenta em catalogo_pronto/images
            candidate_data = data_images_root / rel_no_images_prefix
            if candidate_data.exists():
                return candidate_data
            # Fallback para static
            return static_root / rel

        def safe_attach_image(instance, field_name: str, json_path: str):
            if not json_path:
                return
            # Caminho relativo esperado (ex.: images/xxx.png)
            rel = json_path.lstrip('/')
            if rel.startswith('assets/'):
                rel = rel.replace('assets/', '', 1)
            source_static = static_root / rel  # mantém 'images/...'
            rel_no_images_prefix = rel[7:] if rel.startswith('images/') else rel
            target_data = data_images_root / rel_no_images_prefix

            # Se existir no static e não no catalogo_pronto, copia para organizar na pasta catalogo_pronto/images
            try:
                if source_static.exists() and not target_data.exists():
                    target_data.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source_static, target_data)
            except Exception:
                # Se falhar a cópia, seguimos com fallback
                pass

            img_path = image_path_from_json(json_path)
            if img_path.exists():
                with open(img_path, 'rb') as fh:
                    getattr(instance, field_name).save(img_path.name, File(fh), save=False)
            else:
                self.stdout.write(self.style.WARNING(f"Imagem não encontrada: {json_path} -> {img_path}"))

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
        comidas_json = project_root / 'catalogo_pronto' / 'comidas.json'
        
        if comidas_json.exists():
            with open(comidas_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            cardapio = data.get('cardapio', {})
            
            # Processa comidas
            for item in cardapio.get('comidas', []):
                ic = ItemCardapio(
                    nome=item['nome'],
                    descricao=item['descricao'],
                    categoria=categorias['comidas'],
                )
                safe_attach_image(ic, 'imagem', item.get('imagem', ''))
                ic.save()
                self.stdout.write(f'  - Criado: {item["nome"]}')
            
            # Processa bebidas
            for item in cardapio.get('bebidas', []):
                ic = ItemCardapio(
                    nome=item['nome'],
                    descricao=item['descricao'],
                    categoria=categorias['bebidas'],
                )
                safe_attach_image(ic, 'imagem', item.get('imagem', ''))
                ic.save()
                self.stdout.write(f'  - Criado: {item["nome"]}')
            
            # Processa sobremesas
            for item in cardapio.get('sobremesas', []):
                ic = ItemCardapio(
                    nome=item['nome'],
                    descricao=item['descricao'],
                    categoria=categorias['sobremesas'],
                )
                safe_attach_image(ic, 'imagem', item.get('imagem', ''))
                ic.save()
                self.stdout.write(f'  - Criado: {item["nome"]}')
        
        # Popula jogos
        self.stdout.write('Populando jogos...')
        jogos_json = project_root / 'catalogo_pronto' / 'jogos.json'
        
        if jogos_json.exists():
            with open(jogos_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            jogos_data = data.get('jogos', {})
            
            # Processa jogos de tabuleiro
            for item in jogos_data.get('tabuleiro', []):
                jogo = Jogo(
                    nome=item['nome'],
                    tipo=item['tipo'],
                    descricao=item.get('descricao', ''),
                    categoria=categorias['tabuleiro'],
                )
                safe_attach_image(jogo, 'imagem', item.get('imagem', ''))
                jogo.save()
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
                jogo = Jogo(
                    nome=item['nome'],
                    tipo=item['tipo'],
                    descricao=item.get('descricao', ''),
                    categoria=categorias['maquinas'],
                )
                safe_attach_image(jogo, 'imagem', item.get('imagem', ''))
                jogo.save()
                self.stdout.write(f'  - Criado: {item["nome"]}')
                
                # Cria 1 cópia para cada máquina (geralmente só há uma)
                CopiaJogo.objects.create(
                    jogo=jogo,
                    identificador=f'{jogo.nome[:3].upper()}-001',
                    disponivel=True,
                    uso_atual=None
                )
                self.stdout.write(f'    - Cópia criada: {jogo.nome[:3].upper()}-001')
        
        self.stdout.write(self.style.SUCCESS('\nBanco de dados populado com sucesso (com imagens)!'))
