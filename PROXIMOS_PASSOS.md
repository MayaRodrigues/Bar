# 🚀 Próximos Passos - Luna & Hops Tavern

## ✅ O que foi feito

A nova versão Django do site está **completamente implementada** com:
- ✅ Modelos de banco de dados
- ✅ Django Admin customizado
- ✅ Views dinâmicas
- ✅ Templates atualizados
- ✅ Sistema de rastreamento de disponibilidade de jogos
- ✅ Formulários inline
- ✅ Comando de população do banco

## 🎯 Como Executar o Projeto

### **Opção 1: Script Automatizado (Recomendado)**

Execute o script PowerShell que automatiza todo o processo:

```powershell
.\setup_django.ps1
```

Este script irá:
1. Criar/ativar o ambiente virtual (se necessário)
2. Instalar dependências
3. Executar migrações
4. Perguntar se deseja criar superusuário
5. Perguntar se deseja popular o banco com o catálogo pronto (`catalogo_pronto/`)

### **Opção 2: Passo a Passo Manual**

```bash
# 1. Ativar ambiente virtual
.\venv\Scripts\Activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar migrações
python manage.py makemigrations
python manage.py migrate

# 4. Criar superusuário
python manage.py createsuperuser

# 5. Popular banco de dados
python manage.py popular_banco

# 6. Iniciar servidor
python manage.py runserver
```

## 🌐 Acessando o Sistema

Após iniciar o servidor com `python manage.py runserver`:

### **Site Público:**
- **Página Inicial:** http://127.0.0.1:8000/
- **Cardápio:** http://127.0.0.1:8000/cardapio-comida/
- **Jogos:** http://127.0.0.1:8000/cardapio-jogos/

### **Django Admin:**
- **URL:** http://127.0.0.1:8000/admin/
- **Login:** Use as credenciais criadas no `createsuperuser`

## 📝 Tarefas Importantes

### **1. Imagens do cardápio/jogos**

O comando `popular_banco` agora importa automaticamente as imagens para o banco a partir de `catalogo_pronto/images/...`, conforme os caminhos definidos nos JSONs (`/assets/images/...`). Use o Admin apenas para alterações manuais posteriores (substituições/novos itens).

### **2. Testar Funcionalidade de Disponibilidade**

1. Acesse o Admin: http://127.0.0.1:8000/admin/
2. Vá em "Cópias de Jogos"
3. Teste marcar jogos como disponíveis/indisponíveis
4. Especifique localização (ex: "Mesa 3")
5. Acesse a página de jogos pública e veja a atualização em tempo real

### **3. Testar CRUD Completo**

Teste todas as operações no Django Admin:

**Criar:**
- Adicione uma nova categoria
- Adicione um novo item ao cardápio
- Adicione um novo jogo
- Adicione cópias do jogo (via inline)

**Ler:**
- Navegue pelas listas
- Use os filtros laterais
- Teste a busca

**Atualizar:**
- Edite um item existente
- Use a edição rápida em "Cópias de Jogos"

**Deletar:**
- Delete um item de teste
- Verifique a confirmação

## 🎮 Demonstração da Funcionalidade de Jogos

Para demonstrar o sistema de disponibilidade:

1. **Criar um jogo com múltiplas cópias:**
   - Admin → Jogos → Adicionar
   - Preencha nome, tipo, descrição
   - Na seção inline, adicione 3 cópias:
     - Cópia 1: Disponível
     - Cópia 2: Em Uso - Mesa 1
     - Cópia 3: Em Uso - Mesa 5

2. **Ver no site público:**
   - Acesse http://127.0.0.1:8000/cardapio-jogos/
   - Veja: "1 de 3 cópia(s) disponível(is)"

3. **Atualizar disponibilidade:**
   - Admin → Cópias de Jogos
   - Marque Cópia 2 como Disponível
   - Limpe o campo "Uso atual"
   - Salve
   - Recarregue a página pública
   - Veja: "2 de 3 cópia(s) disponível(is)"

## 📚 Documentação Disponível

- **DJANGO_SETUP.md** - Guia completo de configuração e uso
- **REQUISITOS_ATENDIDOS.md** - Checklist de todos os requisitos
- **README.md** - Documentação geral do projeto
- **PROXIMOS_PASSOS.md** - Este arquivo

## 🔧 Comandos Úteis

```bash
# Criar novas migrações após alterar models.py
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário adicional
python manage.py createsuperuser

# Repopular banco (APAGA DADOS EXISTENTES!)
python manage.py popular_banco

# Abrir shell Django para testes
python manage.py shell

# Coletar arquivos estáticos (para produção)
python manage.py collectstatic
```

## 🎨 Customizações Futuras (Opcional)

Se quiser expandir o projeto:

1. **Adicionar mais campos aos modelos:**
   - Preço nos itens do cardápio
   - Número de jogadores nos jogos
   - Tempo de duração dos jogos

2. **Criar mais views:**
   - Página de detalhes de cada jogo
   - Sistema de reserva de jogos
   - Histórico de uso

3. **Melhorar o Admin:**
   - Adicionar mais filtros
   - Criar actions customizadas
   - Adicionar gráficos de disponibilidade

4. **Adicionar autenticação:**
   - Login para funcionários
   - Diferentes níveis de permissão

## ⚠️ Avisos Importantes

1. **Não execute `popular_banco` após adicionar imagens manualmente** - Ele apaga todos os dados!

2. **O arquivo `db.sqlite3` contém todos os dados** - Faça backup se necessário

3. **Uploads em filesystem** (se houver) vão para `uploads/` (renomeado de `media/`). Por padrão, imagens dos modelos são salvas no banco.

4. **Em produção, configure:**
   - `DEBUG = False` em settings.py
   - `ALLOWED_HOSTS` apropriado
   - Servidor de arquivos estáticos/media adequado

## 🐛 Solução de Problemas Comuns

### Erro: "No module named 'PIL'"
```bash
pip install Pillow
```

### Erro: "Table doesn't exist"
```bash
python manage.py migrate
```

### Imagens não aparecem
1. Verifique se rodou `python manage.py popular_banco` ou fez upload via Admin
2. Verifique se o servidor está rodando
3. As imagens dos modelos são servidas por `/files/get/?name=...` (storage em banco). Os estáticos (logo/slider/fundo) ficam em `cardapio/static/images`.

### CSS não carrega
1. Verifique se `STATICFILES_DIRS` está configurado em settings.py
2. Verifique o caminho no template: `{% static 'css/style.css' %}`

## ✨ Pronto para Apresentar!

O projeto está **completo e funcional**. Todos os requisitos foram atendidos:

- ✅ Páginas dinâmicas com Django
- ✅ Banco de dados com modelos
- ✅ CRUD completo via Admin
- ✅ Customização do Admin
- ✅ Formulários inline
- ✅ Sistema de disponibilidade de jogos

**Boa sorte na apresentação!** 🎉

---

**Desenvolvido por:**
- Mayara Rodrigues Pereira @MayaRodrigues
- Vitor Eduardo de Lima Kenor @VitorEduardoLimaKenor

**Luna & Hops Tavern** 🌙🍺🎲
