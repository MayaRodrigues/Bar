# 📸 Como Adicionar Imagens aos Cardápios

## 🎯 Visão Geral

Os cards dos cardápios agora suportam imagens! Você pode adicionar fotos de cada comida, bebida, sobremesa ou jogo para tornar o site mais atrativo.

## 📁 Estrutura de Diretórios para Imagens

Organize suas imagens na pasta `assets/images/`:

```
Bar/
├── assets/
│   ├── images/
│   │   ├── comidas/
│   │   │   ├── pizza-constelacao.jpg
│   │   │   ├── hamburguer-heroi.jpg
│   │   │   └── ...
│   │   ├── bebidas/
│   │   │   ├── cerveja-dragao.jpg
│   │   │   ├── hidromel.jpg
│   │   │   └── ...
│   │   ├── sobremesas/
│   │   │   ├── doce-lua.jpg
│   │   │   └── ...
│   │   ├── pocoes/
│   │   │   └── pocao-coragem.jpg
│   │   └── jogos/
│   │       ├── tabuleiro/
│   │       │   ├── dnd.jpg
│   │       │   └── ...
│   │       └── maquinas/
│   │           ├── street-fighter.jpg
│   │           └── ...
```

## 📝 Formato do JSON com Imagens

### **Para Comidas/Bebidas (comidas.json)**

```json
{
  "cardapio": {
    "comidas": [
      { 
        "nome": "Pizza da Constelação", 
        "descricao": "Pizza artesanal com ingredientes cósmicos e borda lunar",
        "imagem": "/assets/images/comidas/pizza-constelacao.jpg"
      },
      { 
        "nome": "Hambúrguer do Herói", 
        "descricao": "Hambúrguer suculento com queijo encantado e molho de bravura",
        "imagem": "/assets/images/comidas/hamburguer-heroi.jpg"
      }
    ],
    "bebidas": [
      { 
        "nome": "Cerveja do Dragão", 
        "descricao": "Cerveja encorpada com espuma flamejante",
        "imagem": "/assets/images/bebidas/cerveja-dragao.jpg"
      }
    ],
    "sobremesas": [
      { 
        "nome": "Doce da Lua Cheia", 
        "descricao": "Cheesecake com calda de frutas vermelhas e brilho lunar",
        "imagem": "/assets/images/sobremesas/doce-lua.jpg"
      }
    ],
    "poções_especiais": [
      { 
        "nome": "Poção da Coragem", 
        "descricao": "Mistura cítrica com toque de gengibre e energia solar",
        "imagem": "/assets/images/pocoes/pocao-coragem.jpg"
      }
    ]
  }
}
```

### **Para Jogos (jogos.json)**

```json
{
  "jogos": {
    "tabuleiro": [
      { 
        "nome": "Dungeons & Dragons", 
        "tipo": "RPG de fantasia",
        "imagem": "/assets/images/jogos/tabuleiro/dnd.jpg"
      },
      { 
        "nome": "Catan", 
        "tipo": "Jogo de construção e comércio",
        "imagem": "/assets/images/jogos/tabuleiro/catan.jpg"
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

## ✅ Passo a Passo para Adicionar Imagens

### **1. Prepare as Imagens**
- Formato recomendado: **JPG** ou **PNG**
- Tamanho recomendado: **286x180px** (exato) ou proporção similar (16:10)
- Peso: Máximo **500KB** por imagem (para carregamento rápido)
- Nome do arquivo: Use nomes descritivos sem espaços (ex: `pizza-constelacao.jpg`)

### **2. Organize as Imagens nas Pastas**
Coloque cada imagem na pasta correspondente:
- Comidas → `assets/images/comidas/`
- Bebidas → `assets/images/bebidas/`
- Sobremesas → `assets/images/sobremesas/`
- Poções → `assets/images/pocoes/`
- Jogos de Tabuleiro → `assets/images/jogos/tabuleiro/`
- Máquinas Arcade → `assets/images/jogos/maquinas/`

### **3. Adicione o Campo "imagem" no JSON**
Edite o arquivo JSON correspondente e adicione o campo `"imagem"` com o caminho da imagem:

```json
{
  "nome": "Nome do Item",
  "descricao": "Descrição do item",
  "imagem": "/assets/images/categoria/nome-arquivo.jpg"
}
```

### **4. Execute o Script para Regenerar os Cardápios**
```bash
cd scripts
python gerar_cardapios.py
```

Digite `todos` para regenerar todos os cardápios ou especifique o arquivo JSON.

### **5. Verifique o Resultado**
Os arquivos HTML serão atualizados e abertos automaticamente no navegador com as imagens!

## 🎨 Características dos Cards com Imagens

### **Design Responsivo**
- ✅ Cards com tamanho fixo de **286x180px** (imagem)
- ✅ Grid adaptável que centraliza os cards
- ✅ Efeito hover (card sobe ao passar o mouse)
- ✅ Sombras e bordas arredondadas

### **Estrutura do Card**
```
┌─────────────────────┐
│                     │
│  IMAGEM 286x180px   │  ← Tamanho fixo
│                     │
├─────────────────────┤
│  Título (h3)        │
│  Descrição (p)      │
└─────────────────────┘
```

## 🔄 Compatibilidade com Itens Sem Imagem

**O campo "imagem" é OPCIONAL!** Se você não adicionar o campo `"imagem"`, o card será gerado normalmente apenas com texto:

```json
{
  "nome": "Item Sem Imagem",
  "descricao": "Este item não tem imagem e funcionará normalmente"
}
```

Resultado: Card apenas com título e descrição (sem espaço para imagem).

## 💡 Dicas e Boas Práticas

### **Nomenclatura de Arquivos**
✅ **BOM**: `pizza-constelacao.jpg`, `cerveja-dragao.jpg`  
❌ **RUIM**: `Pizza da Constelação.jpg`, `foto 1.jpg`

### **Otimização de Imagens**
- Use ferramentas como [TinyPNG](https://tinypng.com/) para comprimir imagens
- Mantenha tamanho consistente: **286x180px** para melhor resultado
- Evite imagens muito grandes (acima de 1MB)

### **Caminhos das Imagens**
- Sempre use caminhos absolutos começando com `/assets/`
- Não use caminhos relativos como `../assets/` ou `./images/`
- Certifique-se de que o caminho corresponde exatamente à localização do arquivo

### **Imagens Placeholder**
Se não tiver uma imagem específica, você pode:
1. Deixar o campo `"imagem"` vazio ou omiti-lo
2. Usar uma imagem genérica: `"/assets/images/placeholder.jpg"`

## 🖼️ Exemplo Completo

Veja o arquivo `data/exemplo_com_imagens.json` para um exemplo completo de como estruturar o JSON com imagens.

## 🛠️ Solução de Problemas

### **Imagem não aparece**
- ✅ Verifique se o caminho está correto
- ✅ Confirme que o arquivo existe na pasta
- ✅ Verifique a extensão do arquivo (.jpg, .png)
- ✅ Regenere o HTML executando o script novamente

### **Imagem aparece distorcida**
- ✅ Use `object-fit: cover` (já configurado no CSS)
- ✅ Mantenha proporção de aspecto consistente

### **Site carrega lento**
- ✅ Comprima as imagens
- ✅ Reduza o tamanho dos arquivos
- ✅ Use formato JPG para fotos (menor que PNG)

## 📊 Resumo Rápido

| Aspecto | Valor |
|---------|-------|
| **Campo no JSON** | `"imagem": "/assets/images/categoria/arquivo.jpg"` |
| **Tamanho recomendado** | **286x180px** |
| **Peso máximo** | 500KB |
| **Formatos aceitos** | JPG, PNG, WebP |
| **Campo obrigatório?** | ❌ Não (opcional) |
| **Tamanho no card** | **286x180px** (fixo) |

---

**Agora seus cardápios terão imagens lindas! 🎨📸**
