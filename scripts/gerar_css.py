import os

# Conteúdo padrão do CSS
DEFAULT_STYLE_CSS = """*{
    margin: 0px;
    padding: 0px;
}
html { box-sizing: border-box; overflow-x: hidden; }
*, *::before, *::after { box-sizing: inherit; }
body { overflow-x: hidden; }

:root {
  --color-bg: #1b1c34;
  --color-surface: #2a2b4a;
  --color-primary: #13142f;
  --color-accent: #ffd700;
  --color-text: #f4f4f4;
  --color-muted: #cfcfe6;
  --shadow-1: 0 6px 20px rgba(0,0,0,0.3);
}

html { scroll-behavior: smooth; }

body {
  background: radial-gradient(1200px 800px at 80% -200px, rgba(255,215,0,0.06), transparent 60%), var(--color-bg);
  color: var(--color-text);
  font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  line-height: 1.6;
}

img { max-width: 100%; height: auto; display: block; }

.container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }

.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  box-shadow: var(--shadow-1);
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo img {
  width: 60px;
  height: auto;
}

.titulo {
  color: var(--color-text);
  font-family: 'Cinzel', serif;
  font-size: 22px;
  margin: 0;
  letter-spacing: 0.3px;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 20px;
  margin: 0;
  padding: 0;
}

.submenu {
  position: relative;
}

.dropdown {
  display: none;
  position: absolute;
  background: #222;
  list-style: none;
  padding: 0;
  margin: 0;
  top: 100%;
  left: 0;
  min-width: 150px;
  z-index: 10;
}

.submenu:hover .dropdown {
  display: block;
}

.dropdown li a {
  display: block;
  padding: 10px;
  color: #fff;
  text-decoration: none;
}

.dropdown li a:hover {
  background: #444;
}

.nav-links li a {
  color: var(--color-text);
  text-decoration: none;
  font-family: 'Cinzel', serif;
  font-size: 18px;
  padding: 6px 10px;
  border-radius: 8px;
  transition: color 0.3s ease, background-color 0.3s ease;
}

.nav-links li a:hover,
.nav-links li a.active {
  color: var(--color-accent);
  background-color: rgba(255, 215, 0, 0.06);
}

.slider {
  width: 100%;
  max-width: 100vw;
  height: 640px;
  position: relative;
  overflow: hidden;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.slides {
  position: relative;
  width: 100%;
  height: 100%; 
  position: relative;
}
.slides input[type = "radio"] {
  display: none;
}

.slide {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
  transition: opacity 0.5s;
}

.slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

#radio1:checked ~ .first,
#radio2:checked ~ .slide:nth-of-type(2),
#radio3:checked ~ .slide:nth-of-type(3),
#radio4:checked ~ .slide:nth-of-type(4) {
  opacity: 1;
  position: relative;
}

.navigation-manual {
  position: absolute;
  width: 100%;
  bottom: 10px;
  display: flex;
  justify-content: center;
  gap: 10px;
}

.manual-btn {
  border: 2px solid #fff;
  padding: 5px;
  border-radius: 50%;
  background: #333;
}

.manual-btn:hover { background: var(--color-accent); border-color: var(--color-accent); }

 .bem-vindos {
    background: url('../assets/images/fundo-estrelado.png') no-repeat center center;
  background-size: cover;
  position: relative;
  background-color: var(--color-surface);
  color: var(--color-text);
  padding: 72px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
}

.bem-vindos p { color: var(--color-muted); }


 .section#historia {
  background: url('../assets/images/fundo-estrelado.png') no-repeat center center;
  background-size: cover;
  position: relative;
  padding: 96px 20px;
  color: var(--color-text);
  text-align: center;
}

.section#historia::before {
  content: "";
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: #2a2b4a9a;
 /* background: #13142fd9; /* camada escura sobre o fundo estrelado */
  z-index: -1;
}

.section#historia h2 {
  font-family: 'Cinzel', serif;
  font-size: clamp(26px, 4vw, 36px);
  color: var(--color-accent);
  margin-bottom: 40px;
  text-shadow: 0 0 10px rgba(255, 215, 0, 0.25);
}

.section#historia p {
  font-size: 18px;
  line-height: 1.8;
  margin-bottom: 20px;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
  color: var(--color-muted);
}

.section#historia b {
  color: var(--color-accent);
  font-weight: bold;
}

/* Seções genéricas (Cardápio, Jogos) */
.section {
  padding: 72px 20px;
}

.section h2 {
  font-family: 'Cinzel', serif;
  color: var(--color-accent);
  text-align: center;
  margin-bottom: 16px;
}

.section p {
  color: var(--color-muted);
  text-align: center;
}

footer {
  background-color: var(--color-primary);
  color: var(--color-text);
  text-align: center;
  padding: 15px;
 /* position: fixed;*/
  bottom: 0;
  left: 0;
  width: 100%;
}

/* Cards de Cardápio */
.card {
  background-color: var(--color-primary);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;   /* imagem em cima, conteúdo embaixo */
  width: 100%;              /* ocupa a coluna do grid */
  max-width: 320px;         /* limita largura máxima por card */
  height: 420px;            /* padroniza a altura dos cards */
  text-align: center;
}


.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.5);
}

.card-image {
  width: 100%;
  height: 200px;           /* mesma altura para todas as imagens */
  object-fit: cover;       /* corta e centraliza para preencher */
  object-position: center;
  background-color: var(--color-surface);
  display: block;
}

.card-content {
  padding: 16px 20px;
  flex: 1;                   /* ocupa o restante do card para igualar alturas */
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: center;
}

.card h3 {
  font-family: 'Cinzel', serif;
  color: var(--color-accent);
  font-size: 20px;
  margin-bottom: 10px;
}

.card p {
  color: var(--color-muted);
  font-size: 15px;
  line-height: 1.5;
  margin: 0;
}

/* Grid de Cards */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  justify-items: center;     /* centraliza cards em suas colunas */
  align-items: stretch;      /* garante alturas consistentes */
  gap: 24px;                 /* espaço entre cards */
  margin: 40px auto;
  max-width: 1200px;         /* limita largura do container */
  padding: 0 20px;
}


/* Responsividade */
@media (max-width: 1024px) {
  .titulo { font-size: 20px; }
  .cards-grid {
    gap: 20px;
  }
}

@media (max-width: 768px) {
  .navbar { flex-wrap: wrap; gap: 10px; padding: 10px 16px; }
  .nav-links { width: 100%; justify-content: center; flex-wrap: wrap; gap: 10px 14px; }
  .nav-links li a { font-size: 16px; }
  .slider { height: clamp(220px, 42vh, 420px); }
  .bem-vindos { padding: 56px 0; }
  .section { padding: 56px 20px; }
  .cards-grid {
    gap: 16px;
  }
  .card-content {
    padding: 16px;
  }
  .card h3 {
    font-size: 18px;
  }
  .card p {
    font-size: 14px;
  }
}

@media (max-width: 480px) {
  .logo img { width: 48px; }
  .titulo { font-size: 18px; }
  .nav-links { gap: 8px 12px; }
  .cards-grid {
    gap: 16px;
    flex-direction: column;
    align-items: center;
  }
}
"""

def ensure_style_css(css_path: str, css_content: str | None = None) -> None:
    """Garante que o arquivo CSS exista. Cria apenas se estiver ausente.

    Args:
        css_path: Caminho completo para o style.css de saída.
        css_content: Conteúdo para escrever (opcional). Se None, usa DEFAULT_STYLE_CSS.
    """
    if os.path.exists(css_path):
        return
    os.makedirs(os.path.dirname(css_path), exist_ok=True)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content or DEFAULT_STYLE_CSS)
    print(f"🧩 CSS criado em {css_path}")
