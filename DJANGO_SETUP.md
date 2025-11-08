# 🍺 Luna & Hops Tavern - Versão Django

## 📖 Sobre Esta Versão

Esta é a nova versão do site do bar de jogos, agora desenvolvida com **Django Framework**. As principais mudanças incluem:

- ✅ **Páginas geradas dinamicamente** a partir do banco de dados Django
- ✅ **Sistema de gerenciamento via Django Admin** para CRUD completo
- ✅ **Rastreamento de disponibilidade de jogos** em tempo real
- ✅ **Formulários inline** para gerenciar cópias de jogos
- ✅ **Customização completa do Django Admin**

## 🚀 Como Configurar e Executar

### **Passo 1: Instalar Dependências**

Certifique-se de que o ambiente virtual está ativado e instale as dependências:

```bash
# Ativar ambiente virtual (se ainda não estiver ativo)
.\venv\Scripts\Activate

# Instalar dependências
pip install -r requirements.txt
```

### **Passo 2: Executar Migrações**

Crie as tabelas no banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

### **Passo 3: Criar Superusuário**

Crie um usuário administrador para acessar o Django Admin:

```bash
python manage.py createsuperuser
```

Siga as instruções e forneça:
- Nome de usuário
- Email (opcional)
- Senha

### **Passo 4: Popular o Banco de Dados**

Execute o comando customizado para popular o banco com os dados dos arquivos JSON:

```bash
python manage.py popular_banco
```

Este comando irá:
- Criar todas as categorias (Comidas, Bebidas, Sobremesas, Jogos de Tabuleiro, Máquinas)
- Importar todos os itens do cardápio
- Importar todos os jogos
- Criar cópias de exemplo para cada jogo

### **Passo 5: Iniciar o Servidor**

```bash
python manage.py runserver
```

O servidor estará disponível em: **http://127.0.0.1:8000/**

## 🎯 Acessando o Sistema

### **Site Público**
- **Página Inicial**: http://127.0.0.1:8000/
- **Cardápio**: http://127.0.0.1:8000/cardapio-comida/
- **Jogos**: http://127.0.0.1:8000/cardapio-jogos/

### **Django Admin**
- **URL**: http://127.0.0.1:8000/admin/
- **Login**: Use as credenciais do superusuário criado no Passo 3

## 📋 Funcionalidades do Django Admin

### **1. Gerenciamento de Categorias**
- Criar, editar e remover categorias
- Definir ícones/emojis para cada categoria
- Slug automático baseado no nome

### **2. Gerenciamento de Itens do Cardápio**
- CRUD completo de comidas, bebidas e sobremesas
- Upload de imagens
- Filtros por categoria
- Busca por nome e descrição

### **3. Gerenciamento de Jogos**
- CRUD completo de jogos
- Upload de imagens
- Visualização de total de cópias e cópias disponíveis
- **Formulários Inline** para gerenciar cópias diretamente na página do jogo

### **4. Gerenciamento de Cópias de Jogos**
- Registrar quais jogos estão sendo utilizados
- Marcar disponibilidade (Disponível/Em Uso)
- Especificar localização atual (ex: "Mesa 5")
- **Edição rápida na lista** - altere disponibilidade sem abrir o formulário completo
- Indicadores visuais de status (✅ Disponível / 🔴 Em Uso)

## 🎮 Rastreamento de Disponibilidade de Jogos

### **Como Funciona:**

1. Cada jogo pode ter múltiplas cópias físicas
2. Cada cópia tem um identificador único (ex: "DND-001", "DND-002")
3. Funcionários podem marcar cópias como:
   - **Disponível**: Jogo está livre para uso
   - **Em Uso**: Jogo está sendo utilizado (com informação de onde)

### **No Site Público:**

Na página de jogos, os clientes podem ver:
- Total de cópias de cada jogo
- Quantas cópias estão disponíveis no momento
- Exemplo: "2 de 3 cópia(s) disponível(is)"

### **No Django Admin:**

Funcionários podem:
- Adicionar novas cópias de jogos
- Marcar cópias como disponíveis ou em uso
- Especificar onde o jogo está sendo usado (Mesa 1, Mesa 2, etc.)
- Editar rapidamente o status diretamente na lista

## 📁 Estrutura do Projeto

```
Bar/
├── cardapio/                      # App principal
│   ├── management/
│   │   └── commands/
│   │       └── popular_banco.py   # Comando para popular BD
│   ├── migrations/                # Migrações do banco
│   ├── templates/
│   │   └── cardapio/
│   │       ├── index.html         # Página inicial (Django template)
│   │       ├── cardapio_comida.html  # Cardápio dinâmico
│   │       └── cardapio_jogos.html   # Jogos com disponibilidade
│   ├── admin.py                   # Configuração do Django Admin
│   ├── models.py                  # Modelos do banco de dados
│   ├── views.py                   # Views dinâmicas
│   └── urls.py                    # URLs do app
├── bar_core/                      # Configurações do projeto
│   ├── settings.py
│   └── urls.py
├── data/                          # Arquivos JSON originais
│   ├── comidas.json
│   └── jogos.json
├── media/                         # Uploads de imagens (criado automaticamente)
├── db.sqlite3                     # Banco de dados SQLite
├── manage.py
└── requirements.txt
```

## 🔄 Atualizando Dados

### **Via Django Admin (Recomendado)**

1. Acesse http://127.0.0.1:8000/admin/
2. Navegue até o modelo desejado (Categorias, Itens do Cardápio, Jogos, etc.)
3. Use os botões:
   - **Adicionar** para criar novos registros
   - **Editar** (ícone de lápis) para modificar existentes
   - **Deletar** para remover registros

### **Via Comando de Gerenciamento**

Para repopular o banco a partir dos JSONs:

```bash
python manage.py popular_banco
```

⚠️ **ATENÇÃO**: Este comando apaga todos os dados existentes!

## 🎨 Adicionando Imagens

### **Método 1: Via Django Admin**

1. Acesse o Django Admin
2. Edite um item do cardápio ou jogo
3. Clique em "Choose File" no campo de imagem
4. Faça upload da imagem
5. Salve

### **Método 2: Copiar Imagens Existentes**

As imagens dos arquivos estáticos podem ser copiadas para a pasta `media/`:

```bash
# Criar estrutura de pastas
mkdir media\cardapio_imagens
mkdir media\jogos_imagens

# Copiar imagens (exemplo)
# Depois adicione via admin ou ajuste o comando popular_banco.py
```

## 📊 Modelos do Banco de Dados

### **Categoria**
- `nome`: Nome da categoria
- `slug`: Identificador único para URLs
- `icone`: Emoji/ícone da categoria

### **ItemCardapio**
- `nome`: Nome do item
- `descricao`: Descrição detalhada
- `imagem`: Upload de imagem
- `categoria`: Relacionamento com Categoria

### **Jogo**
- `nome`: Nome do jogo
- `tipo`: Tipo/gênero do jogo
- `descricao`: Descrição detalhada
- `imagem`: Upload de imagem
- `categoria`: Relacionamento com Categoria

### **CopiaJogo**
- `jogo`: Relacionamento com Jogo
- `identificador`: ID único da cópia (ex: "DND-001")
- `disponivel`: Boolean (True/False)
- `uso_atual`: Onde está sendo usado (opcional)

## 🛠️ Customizações do Django Admin

### **Recursos Implementados:**

1. **Lista Customizada**
   - Colunas personalizadas para cada modelo
   - Métodos customizados para exibir informações calculadas
   - Ordenação inteligente

2. **Filtros e Busca**
   - Filtros laterais por categoria, tipo, disponibilidade
   - Busca por nome, descrição, identificador

3. **Formulários Inline**
   - Gerenciar cópias de jogos diretamente na página do jogo
   - Adicionar múltiplas cópias de uma vez

4. **Edição Rápida**
   - `list_editable` permite editar disponibilidade e localização sem abrir formulário

5. **Campos Auto-preenchidos**
   - Slug gerado automaticamente a partir do nome

## 🔒 Requisitos Atendidos

✅ **Utilizar banco de dados via modelos do Django**
- Modelos: Categoria, ItemCardapio, Jogo, CopiaJogo

✅ **CRUD via Django Admin**
- Criação, leitura, atualização e remoção de todos os dados

✅ **Customização da lista de objetos**
- `list_display`, `list_filter`, `search_fields`, `ordering`

✅ **Formulários inline**
- `CopiaJogoInline` para gerenciar cópias na página do jogo

✅ **Funcionalidade de registro de disponibilidade**
- Modelo `CopiaJogo` com campos `disponivel` e `uso_atual`
- Edição rápida via `list_editable`

✅ **Informação de disponibilidade no site**
- Método `copias_disponiveis()` no modelo Jogo
- Exibição na página de jogos

## 💡 Dicas de Uso

### **Para Funcionários:**

1. **Registrar Uso de Jogo:**
   - Admin → Cópias de Jogos
   - Encontre a cópia do jogo
   - Marque "Disponível" como False
   - Preencha "Uso atual" (ex: "Mesa 3")
   - Salve

2. **Liberar Jogo:**
   - Marque "Disponível" como True
   - Limpe o campo "Uso atual"
   - Salve

3. **Adicionar Novo Jogo:**
   - Admin → Jogos → Adicionar Jogo
   - Preencha informações
   - Na seção "Cópias de jogos", adicione as cópias físicas
   - Salve

### **Para Clientes:**

- Acesse a página de Jogos para ver disponibilidade em tempo real
- Indicador verde = cópias disponíveis
- Indicador vermelho = todas as cópias em uso

## 🐛 Solução de Problemas

### **Erro: "No module named 'PIL'"**
```bash
pip install Pillow
```

### **Erro: "Table doesn't exist"**
```bash
python manage.py migrate
```

### **Imagens não aparecem**
- Verifique se `MEDIA_URL` e `MEDIA_ROOT` estão configurados em `settings.py`
- Certifique-se de que as URLs de media estão em `urls.py`
- Faça upload das imagens via Django Admin

### **Comando popular_banco não encontrado**
```bash
# Verifique se a estrutura de pastas está correta:
cardapio/management/commands/popular_banco.py
# E se os __init__.py existem
```

## 📞 Suporte

Para problemas ou dúvidas:
1. Verifique os logs do Django no terminal
2. Acesse o Django Admin para verificar os dados
3. Consulte a documentação oficial do Django: https://docs.djangoproject.com/

---

## 👨‍💻 Autores
- Mayara Rodrigues Pereira @MayaRodrigues
- Vitor Eduardo de Lima Kenor @VitorEduardoLimaKenor

**Desenvolvido para Luna & Hops Tavern** 🌙🍺🎲
