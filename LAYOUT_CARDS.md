# 📐 Layout dos Cards - Flexbox Row Centralizado

## 🎯 Configuração Atual

Os cards agora estão configurados com **Flexbox** em modo **row** (linha), centralizados horizontalmente.

### **Propriedades CSS Aplicadas:**

```css
.cards-grid {
  display: flex;
  flex-direction: row;        /* Cards em linha horizontal */
  flex-wrap: wrap;            /* Quebra para próxima linha quando necessário */
  justify-content: center;    /* Centraliza horizontalmente */
  align-items: flex-start;    /* Alinha no topo */
  gap: 24px;                  /* Espaçamento entre cards */
}

.card {
  width: 286px;               /* Largura fixa */
  height: auto;               /* Altura automática */
}
```

## 📱 Comportamento Responsivo

### **Desktop (> 1024px)**
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│    ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐         │
│    │Card 1│  │Card 2│  │Card 3│  │Card 4│         │
│    └──────┘  └──────┘  └──────┘  └──────┘         │
│                                                     │
│    ┌──────┐  ┌──────┐  ┌──────┐                   │
│    │Card 5│  │Card 6│  │Card 7│                   │
│    └──────┘  └──────┘  └──────┘                   │
│                                                     │
└─────────────────────────────────────────────────────┘
```
- Cards em múltiplas linhas
- Centralizados horizontalmente
- Gap de 24px entre cards

### **Tablet (768px - 1024px)**
```
┌───────────────────────────────────┐
│                                   │
│   ┌──────┐  ┌──────┐  ┌──────┐   │
│   │Card 1│  │Card 2│  │Card 3│   │
│   └──────┘  └──────┘  └──────┘   │
│                                   │
│   ┌──────┐  ┌──────┐             │
│   │Card 4│  │Card 5│             │
│   └──────┘  └──────┘             │
│                                   │
└───────────────────────────────────┘
```
- 2-3 cards por linha
- Gap de 16px
- Centralizados

### **Mobile (< 480px)**
```
┌─────────────────┐
│                 │
│    ┌──────┐     │
│    │Card 1│     │
│    └──────┘     │
│                 │
│    ┌──────┐     │
│    │Card 2│     │
│    └──────┘     │
│                 │
│    ┌──────┐     │
│    │Card 3│     │
│    └──────┘     │
│                 │
└─────────────────┘
```
- 1 card por linha (coluna)
- Centralizados verticalmente
- Gap de 16px

## ✨ Características do Layout

### **Vantagens do Flexbox Row:**
- ✅ **Centralização automática** - Cards sempre centralizados
- ✅ **Responsivo** - Adapta automaticamente ao tamanho da tela
- ✅ **Flexível** - Quebra linha quando necessário
- ✅ **Alinhamento consistente** - Todos os cards alinhados no topo

### **Propriedades Importantes:**

| Propriedade | Valor | Função |
|-------------|-------|--------|
| `display` | `flex` | Ativa o flexbox |
| `flex-direction` | `row` | Cards em linha horizontal |
| `flex-wrap` | `wrap` | Permite quebra de linha |
| `justify-content` | `center` | Centraliza horizontalmente |
| `align-items` | `flex-start` | Alinha no topo |
| `gap` | `24px` | Espaçamento uniforme |

## 🎨 Exemplo Visual Completo

### **Categoria com 10 Cards:**

```
════════════════════════════════════════════════════════
                    🍽️ Comidas
════════════════════════════════════════════════════════

    ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
    │  🍕  │  │  🍔  │  │  🥔  │  │  🍢  │
    │Pizza │  │Burger│  │Batata│  │Espeto│
    └──────┘  └──────┘  └──────┘  └──────┘

    ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
    │  🧀  │  │  🥟  │  │  🥚  │  │  🍲  │
    │Tábua │  │Coxinh│  │Ovo   │  │Ensopa│
    └──────┘  └──────┘  └──────┘  └──────┘

    ┌──────┐  ┌──────┐
    │  🥖  │  │  🧅  │
    │Pão   │  │Anéis │
    └──────┘  └──────┘

════════════════════════════════════════════════════════
```

## 🔧 Customizações Possíveis

### **Alterar número de cards por linha:**
```css
.cards-grid {
  max-width: 1200px; /* Limita largura máxima */
  margin: 0 auto;    /* Centraliza o container */
}
```

### **Alterar espaçamento:**
```css
.cards-grid {
  gap: 30px;         /* Aumenta espaçamento */
  row-gap: 40px;     /* Espaçamento vertical diferente */
  column-gap: 20px;  /* Espaçamento horizontal diferente */
}
```

### **Alterar alinhamento:**
```css
.cards-grid {
  justify-content: flex-start;  /* Alinha à esquerda */
  justify-content: flex-end;    /* Alinha à direita */
  justify-content: space-between; /* Espaça igualmente */
  justify-content: space-around;  /* Espaça com margens */
}
```

## 📊 Resumo Técnico

| Aspecto | Configuração |
|---------|--------------|
| **Layout** | Flexbox Row |
| **Centralização** | Horizontal (justify-content: center) |
| **Quebra de linha** | Automática (flex-wrap: wrap) |
| **Tamanho do card** | 286px (fixo) |
| **Gap desktop** | 24px |
| **Gap mobile** | 16px |
| **Responsividade** | Automática |

---

**Layout otimizado para exibição de cards em linha, centralizados e responsivos! 🎯✨**
