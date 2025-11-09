# 🍺 Luna & Hops Tavern - Sistema de Geração de Cardápios

> **✅ Versão atual: Django (dinâmica, com banco de dados)**  
> O projeto roda em Django com páginas dinâmicas, CRUD pelo Django Admin e imagens armazenadas no banco (via `django-db-file-storage`).  
> **📖 Guia recomendado: [DJANGO_SETUP.md](DJANGO_SETUP.md)**

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
- **📖 [Ver documentação completa](DJANGO_SETUP.md)**  

## 📋 Descrição do Projeto

Este projeto contém um sistema automatizado para gerar páginas HTML de cardápios a partir de arquivos JSON. O script principal é `scripts/site.py`, que utiliza `scripts/gerar_html.py` e `scripts/gerar_css.py` para gerar páginas HTML completas com estilo CSS.

## ⚙️ Tecnologias Utilizadas  
- **HTML5** → Estrutura do site  
- **CSS3** → Estilização das páginas  
- **Python 3** → Script para gerar os cardápios automaticamente  
- **Arquivos de dados** → Formato `.json` para armazenar alimentos, bebidas e jogos  

## 🎯 Requisitos Atendidos

✅ **Geração Automática**: Os cardápios HTML são gerados automaticamente por script Python  
✅ **Dados em Formato Texto**: Utiliza arquivos JSON (não HTML) como fonte de dados  
✅ **Atualização Dinâmica**: Basta executar o script novamente após modificar os arquivos JSON  
✅ **HTML/CSS Gerado**: Todo o HTML e estrutura são gerados pelo script Python  
✅ **Validação de Entrada**: O script valida entradas e não encerra em caso de erro  

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

## 🚀 Como Usar

### **Opção 1: Modo Interativo (Recomendado)**

Execute o script principal sem argumentos para entrar no modo interativo:

```bash
cd scripts
python site.py
```

O script apresentará um menu com opções:

```
============================================================
🍺 Gerador de Cardápios - Luna & Hops Tavern 🎲
============================================================

Opções disponíveis:
  1. Digite o caminho para um arquivo JSON
  2. Digite o caminho para um diretório contendo arquivos JSON
  3. Digite 'todos' para gerar todos os cardápios padrão
  4. Digite 'sair' para encerrar o programa

Exemplos:
  - ..\data\comidas.json
  - ..\data
  - todos
============================================================

📝 Digite sua escolha:
```

**Opções válidas:**
- `todos` - Gera todos os cardápios (comidas e jogos)
- `comidas.json` - Gera apenas o cardápio de comidas
- `jogos.json` - Gera apenas o cardápio de jogos
- `../data` - Processa todos os JSONs no diretório data
- `sair` - Encerra o programa

### **Opção 2: Linha de Comando**

Execute o script passando o caminho do arquivo ou diretório:

```bash
# Gerar cardápio específico
python gerar_cardapios.py ../data/comidas.json

# Processar todos os arquivos em um diretório
python gerar_cardapios.py ../data

# Caminho absoluto
python gerar_cardapios.py "C:\Users\...\Bar\data\jogos.json"
```

## 📝 Formato dos Arquivos JSON

### **comidas.json**

```json
{
  "cardapio": {
    "comidas": [
      { 
        "nome": "Pizza da Constelação", 
        "descricao": "Pizza artesanal...",
        "imagem": "/assets/images/comidas/pizza-constelacao.jpg"
      }
    ],
    "bebidas": [
      { 
        "nome": "Cerveja do Dragão", 
        "descricao": "Cerveja encorpada...",
        "imagem": "/assets/images/bebidas/cerveja-dragao.jpg"
      }
    ],
    "sobremesas": [
      { 
        "nome": "Doce da Lua Cheia", 
        "descricao": "Cheesecake...",
        "imagem": "/assets/images/sobremesas/doce-lua.jpg"
      }
    ],
    "poções_especiais": [
      { 
        "nome": "Poção da Coragem", 
        "descricao": "Mistura cítrica...",
        "imagem": "/assets/images/pocoes/pocao-coragem.jpg"
      }
    ]
  }
}
```

### **jogos.json**

```json
{
  "jogos": {
    "tabuleiro": [
      { 
        "nome": "Dungeons & Dragons", 
        "tipo": "RPG de fantasia",
        "imagem": "/assets/images/jogos/tabuleiro/dnd.jpg"
      }
    ],
    "maquinas": [
      { 
        "nome": "Street Fighter II", 
        "tipo": "Luta clássica arcade",
        "imagem": "/assets/images/jogos/maquinas/street-fighter.jpg"
      }
    ]
  }
}
```

**📸 Nota sobre Imagens:**
- O campo `"imagem"` é opcional — itens sem imagem funcionam normalmente.
- Caminhos aceitos para imagens nos JSONs: `../assets/...`, `/assets/...` ou `assets/...`.
  - Os caminhos iniciando com `/assets/...` ou `assets/...` são normalizados automaticamente para `../assets/...` nas páginas dentro de `site/`.

## 🔄 Atualizando os Cardápios

### **Passo a Passo:**

1. **Edite o arquivo JSON** desejado (`comidas.json` ou `jogos.json`)
   - Adicione novos itens
   - Remova itens existentes
   - Atualize descrições

2. **Execute o script Python**
   ```bash
   python gerar_cardapios.py
   ```

3. **Digite a opção desejada**
   - `todos` para atualizar tudo
   - Nome do arquivo específico para atualizar apenas um cardápio

4. **Os arquivos HTML serão atualizados automaticamente** e abertos no navegador

### **Exemplo de Atualização:**

```json
// Adicionar novo item em comidas.json
{
  "cardapio": {
    "comidas": [
      { "nome": "Pizza da Constelação", "descricao": "Pizza artesanal..." },
      { "nome": "Novo Prato Mágico", "descricao": "Descrição do novo prato" }  // ← NOVO
    ]
  }
}
```

Após salvar, execute:
```bash
python site.py
> Digite: comidas.json
```

## 🛠️ Funcionalidades

✅ Página inicial com apresentação do bar (fotos e vídeos).
✅ Cardápio de alimentos e bebidas gerado automaticamente.
✅ Lista de jogos de tabuleiro com descrição.
✅ Estilo responsivo com CSS.
✅ Possibilidade de atualizar os arquivos de entrada e regenerar o site.




## 🛡️ Validações e Tratamento de Erros

O script possui validações robustas:

✅ **Arquivo não existe**: Mostra erro e pede nova entrada  
✅ **JSON inválido**: Detecta e informa o problema  
✅ **Formato incorreto**: Valida estrutura do JSON  
✅ **Diretório vazio**: Verifica se há arquivos JSON  
✅ **Entrada vazia**: Rejeita e solicita novamente  

**O programa NUNCA encerra devido a entrada incorreta** - sempre oferece nova tentativa!

## 🌐 Arquivos Gerados

O script gera dois arquivos HTML completos:

### **cardapio_comida.html**
- Contém todas as categorias: comidas, bebidas, sobremesas e poções especiais
- Navegação integrada com o site
- Estilo consistente usando `style.css`
- Emojis temáticos por categoria

### **cardapio_jogos.html**
- Lista completa de jogos de tabuleiro e máquinas arcade
- Informações de tipo para cada jogo
- Navegação integrada com o site
- Layout responsivo

## 💡 Dicas

- Use caminhos relativos para facilitar: `comidas.json` em vez de caminho completo
- O script resolve automaticamente caminhos relativos ao diretório `data`
- Digite `todos` para gerar ambos os cardápios de uma vez
- Os arquivos HTML abrem automaticamente no navegador após geração
- Use Ctrl+C para interromper o programa a qualquer momento

## 🎨 Personalização

Para adicionar novas categorias:

1. Adicione a categoria no arquivo JSON
2. (Opcional) Adicione emoji correspondente no script Python:
   ```python
   emoji = {
       "comidas": "🍽️",
       "bebidas": "🍹",
       "nova_categoria": "🎯"  # ← Adicione aqui
   }
   ```

## 📞 Suporte

Se encontrar problemas:
1. Verifique se os arquivos JSON estão no formato correto.
2. Certifique-se de estar no diretório `scripts` ao executar.
3. Verifique as mensagens de erro — elas são descritivas e ajudam a identificar o problema.

---

## 👨‍💻 Autores
 Mayara Rodrigues Pereira @MayaRodrigues
 Vitor Eduardo de Lima Kenor @VitorEduardoLimaKenor

**Desenvolvido para Luna & Hops Tavern** 🌙🍺🎲
