# 📋 Changelog - Sistema de Cardápios

## 🚀 Versão 3.0 – Migração completa para Django (dinâmico)

### Principais mudanças
- Páginas dinâmicas com Django (home, cardápio, jogos)
- CRUD completo via Django Admin com personalizações e inlines
- Rastreamento de disponibilidade de jogos (cópias disponíveis)
- Imagens de modelos armazenadas no banco via `django-db-file-storage`
- Camada de compatibilidade local para servir arquivos: `/files/get/` e `/files/download/`
- Script `setup_django.ps1` automatiza venv, dependências, migrações, superusuário e população
- Comando `popular_banco` importa JSONs e imagens automaticamente
- Pasta renomeada: `data/` → `catalogo_pronto/` (com `images/`)
- Pasta de media renomeada: `media/` → `uploads/`
- Limpeza de estáticos: imagens de modelos saíram de `cardapio/static/images` (mantidos apenas logo/slider/fundo)

### Documentação atualizada
- DJANGO_SETUP.md (setup e operação)
- PROXIMOS_PASSOS.md (execução, dicas e avisos)
- COMO_ADICIONAR_IMAGENS.md (fluxo via Admin e via `catalogo_pronto`)
- README.md (Django como versão atual)
- REQUISITOS_ATENDIDOS.md (armazenamento de imagens no banco)

---
## 🎨 Versão 2.0 - Suporte a Imagens nos Cards

### ✨ Novidades

#### **Cards com Imagens**
- ✅ Suporte completo para imagens nos cards de cardápios
- ✅ Layout responsivo com grid adaptável
- ✅ Efeito hover elegante (card sobe ao passar o mouse)
- ✅ Imagens com altura fixa de 200px e `object-fit: cover`

#### **Estrutura do Card**
```
┌─────────────────────────┐
│                         │
│   IMAGEM (200px)        │
│                         │
├─────────────────────────┤
│   Título                │
│   Descrição             │
└─────────────────────────┘
```

#### **CSS Adicionado**
- `.card` - Estilo base do card com sombras e bordas arredondadas
- `.card-image` - Estilo para as imagens (200px altura, object-fit: cover)
- `.card-content` - Container para título e descrição
- `.cards-grid` - Grid responsivo com auto-fill

#### **Script Python Atualizado**
- Suporte ao campo opcional `"imagem"` no JSON
- Geração automática de HTML com ou sem imagens
- Compatibilidade retroativa (itens sem imagem funcionam normalmente)

### 📝 Formato JSON Atualizado

**Antes:**
```json
{
  "nome": "Pizza da Constelação",
  "descricao": "Pizza artesanal..."
}
```

**Depois:**
```json
{
  "nome": "Pizza da Constelação",
  "descricao": "Pizza artesanal...",
  "imagem": "/assets/images/comidas/pizza-constelacao.jpg"
}
```

### 📱 Responsividade

| Tamanho de Tela | Colunas | Altura da Imagem |
|-----------------|---------|------------------|
| > 1024px        | 3-4     | 200px            |
| 768px - 1024px  | 2-3     | 200px            |
| 480px - 768px   | 1-2     | 180px            |
| < 480px         | 1       | 200px            |

### 📚 Documentação Criada

1. **COMO_ADICIONAR_IMAGENS.md**
   - Guia completo sobre como adicionar imagens
   - Estrutura de diretórios recomendada
   - Boas práticas e otimização
   - Solução de problemas

2. **exemplo_com_imagens.json**
   - Exemplo prático de JSON com imagens
   - Referência para estrutura correta

3. **README.md atualizado**
   - Seção sobre imagens adicionada
   - Exemplos atualizados com campo `"imagem"`

### 🔄 Compatibilidade

- ✅ **100% retrocompatível** - JSONs antigos sem campo `"imagem"` continuam funcionando
- ✅ Campo `"imagem"` é **opcional**
- ✅ Cards sem imagem exibem apenas título e descrição

### 🎯 Benefícios

- **Visual Atrativo**: Cards com imagens são mais chamativos
- **Profissional**: Layout moderno e elegante
- **Flexível**: Funciona com ou sem imagens
- **Responsivo**: Adapta-se a qualquer tamanho de tela

---

## 📦 Versão 1.0 - Sistema Base

### ✨ Funcionalidades Iniciais

- ✅ Geração automática de HTML a partir de JSON
- ✅ Modo interativo com prompt
- ✅ Validação de entrada com loop contínuo
- ✅ Suporte a linha de comando
- ✅ Abertura automática no navegador
- ✅ Templates HTML embutidos
- ✅ Detecção automática de tipo (comida/jogos)
- ✅ Tratamento robusto de erros

### 📝 Arquivos Criados

- `gerar_cardapios.py` - Script principal
- `comidas.json` - Dados de alimentos e bebidas
- `jogos.json` - Dados de jogos
- `README.md` - Documentação completa

---

**Última atualização:** 30/09/2025
