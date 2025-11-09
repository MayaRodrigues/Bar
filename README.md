# 🍺 Luna & Hops Tavern - Sistema de Geração de Cardápios

> **✅ Versão atual: Django (dinâmica, com banco de dados)**  
> O projeto roda em Django com páginas dinâmicas, CRUD pelo Django Admin e imagens armazenadas no banco (via `django-db-file-storage`).

## 📖 Sobre o Projeto  
Este projeto foi desenvolvido como parte da disciplina **Projeto e Desenvolvimento de Sistemas Web (CC6PDSW)**, no curso de **Ciência da Computação – UTFPR**.  

O objetivo é criar um **site de um bar de jogos de tabuleiro** utilizando **HTML, CSS e Python**, onde parte do conteúdo (cardápio de alimentos/bebidas e jogos) é gerado automaticamente a partir de arquivos de entrada.

## 🔄 Versões do Projeto

### **Versão 1 (LEGADO): Geração Estática (Avaliação Anterior)**
- Páginas HTML geradas por scripts Python
- Dados em arquivos JSON
- Documentação neste arquivo

### **Versão 2: Django Framework (Atual)** ⭐
- Páginas geradas dinamicamente pelo Django
- Banco de dados com modelos Django
- Django Admin para CRUD completo
- Rastreamento de disponibilidade de jogos

## 🧩 Funcionalidades (Django)

- Páginas dinâmicas (home, cardápio de comidas/bebidas, jogos) usando templates Django
- Modelos e ORM para categorias, itens de cardápio, jogos e cópias de jogos
- Django Admin customizado com `list_display`, `list_editable`, filtros e inlines para cópias
- Rastreamento de disponibilidade de jogos (cópias disponíveis/em uso)
- Imagens dos modelos armazenadas no banco via `django-db-file-storage`

## 📁 Estrutura de Arquivos (atual)

```
Bar/
├── cardapio/                     # App Django
│   ├── templates/cardapio/       # Templates (index, cardápios)
│   ├── static/                   # Assets de UI (logo, slides, fundo)
│   └── management/commands/      # popular_banco.py
├── bar_core/                     # Configurações do projeto
├── catalogo_pronto/              # JSON + imagens para popular o banco
│   ├── comidas.json
│   ├── jogos.json
│   └── images/
├── uploads/                      # Uploads se algum storage em filesystem for usado
├── setup_django.ps1              # Setup automatizado
└── requirements.txt
```

## 🚀 Como rodar

### **Opção A — Setup automatizado (recomendado - Windows/PowerShell)**
```powershell
./setup_django.ps1
```
O script:
- Cria/ativa a venv (se necessário)
- Instala dependências
- Executa migrações
- Oferece criar superusuário
- Pergunta se deseja popular o banco com o catálogo pronto (`catalogo_pronto/`)

### **Opção B — Passo a passo manual**
```bash
# 1) Ativar venv
.\venv\Scripts\Activate

# 2) Instalar dependências
pip install -r requirements.txt

# 3) Migrações
python manage.py makemigrations
python manage.py migrate

# 4) (Opcional) Criar superusuário
python manage.py createsuperuser

# 5) (Opcional) Popular o banco com JSON + imagens
python manage.py popular_banco

# 6) Subir servidor
python manage.py runserver
```

### URLs importantes
- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 📦 Populando o banco
- JSONs em `catalogo_pronto/` (`comidas.json`, `jogos.json`).
- Imagens referenciadas nos JSONs como `/assets/images/...` são localizadas em `catalogo_pronto/images/...` (com fallback para `cardapio/static/images`).
- O comando `python manage.py popular_banco` apaga dados existentes e recria tudo, anexando as imagens nos modelos.

## 🖼️ Imagens armazenadas no banco
- `DEFAULT_FILE_STORAGE = 'db_file_storage.storage.DatabaseFileStorage'`.
- `ItemCardapio.imagem` e `Jogo.imagem` usam `upload_to` dos FileModels do app.
- Upload pelo Admin salva no banco; ao substituir/limpar, a imagem antiga é removida.
- As URLs das imagens de modelos iniciam com `/files/get/?name=...`.
- Imagens de layout (logo/slider/fundos) continuam em `cardapio/static/images` via `{% static %}`.

## 🔧 Troubleshooting
- Pillow ausente: `pip install Pillow`
- "Table doesn't exist": `python manage.py migrate`
- `popular_banco` não encontrado: confirme `cardapio/management/commands/popular_banco.py` e `__init__.py` nas pastas.
- Imagens não aparecem:
  - Verifique se populou via Admin ou `popular_banco`.
  - Confira URLs `/files/get/?name=...` e se o registro tem imagem.
  - Estáticos continuam em `cardapio/static/images`.

## 📞 Suporte

Se encontrar problemas:
1. Verifique dependências instaladas (Pillow/Django).
2. Rode migrações (`python manage.py migrate`).
3. Valide se `popular_banco` foi executado ou se subiu imagens via Admin.

---

## 👨‍💻 Autores
 Mayara Rodrigues Pereira @MayaRodrigues
 Vitor Eduardo de Lima Kenor @VitorEduardoLimaKenor

**Desenvolvido para Luna & Hops Tavern** 🌙🍺🎲
