from typing import Dict, Any


def normalize_asset_path(path: str) -> str:
    """Normaliza caminhos de assets para funcionar a partir de arquivos em site/.

    Regras:
    - URLs absolutas (http/https/data:) permanecem iguais
    - Outros caminhos retornam como estão
    """
    if not path:
        return path
    lower = path.lower()
    if lower.startswith('http://') or lower.startswith('https://') or lower.startswith('data:'):
        return path
    if path.startswith('../assets/'):
        return path
    if path.startswith('/assets/'):
        return '..' + path
    if path.startswith('assets/'):
        return '../' + path
    return path

def gerar_cardapio_comida(dados: Dict[str, Any]) -> str:
    """Gera o HTML do cardápio de comidas a partir do dicionário já carregado."""
    cardapio = dados["cardapio"]

    html = """<!DOCTYPE html>
    <html lang="pt-BR">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Cardápio - Luna & Hops Tavern</title>
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <header>
        <nav class="navbar">
          <div class="logo">
            <img src="../assets/images/logo.png" alt="Logo do Bar de Jogos">
            <h1 class="titulo">Luna & Hops Tavern</h1>
          </div>
          <ul class="nav-links">
            <li><a href="index.html">Início</a></li>
            <li><a href="cardapio_comida.html" class="active">Cardápio</a></li>
            <li><a href="cardapio_jogos.html">Jogos</a></li>
          </ul>
        </nav>
      </header>
      
      <main>
        <section class="bem-vindos">
          <div class="container">
            <h1>🍽️ Cardápio Mágico</h1>
            {{CONTEUDO}}
          </div>
        </section>
      </main>

      <footer>
        <p>&copy; 2024 Luna & Hops Tavern. | Todos os direitos reservados.</p>
      </footer>
    </body>
    </html>"""

    blocos = ""

    for categoria, itens in cardapio.items():
        emoji = {
            "comidas": "🍽️",
            "bebidas": "🍹",
            "sobremesas": "🍰",
        }.get(categoria, "✨")

        blocos += f"<h2>{emoji} {categoria.replace('_', ' ').title()}</h2><div class='cards-grid'>"

        for item in itens:
            imagem = normalize_asset_path(item.get('imagem', ''))
            if imagem:
                blocos += f"""
            <div class="card">
                <img src="{imagem}" alt="{item['nome']}" class="card-image">
                <div class="card-content">
                    <h3>{item['nome']}</h3>
                    <p>{item['descricao']}</p>
                </div>
            </div>
            """
            else:
                blocos += f"""
            <div class="card">
                <div class="card-content">
                    <h3>{item['nome']}</h3>
                    <p>{item['descricao']}</p>
                </div>
            </div>
            """
        blocos += "</div>"

    return html.replace("{{CONTEUDO}}", blocos)


def gerar_cardapio_jogos(dados: Dict[str, Any]) -> str:
    """Gera o HTML da lista de jogos a partir do dicionário já carregado."""
    jogos = dados["jogos"]

    html = """<!DOCTYPE html>
    <html lang="pt-BR">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Jogos - Luna & Hops Tavern</title>
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <header>
        <nav class="navbar">
          <div class="logo">
            <img src="../assets/images/logo.png" alt="Logo do Bar de Jogos">
            <h1 class="titulo">Luna & Hops Tavern</h1>
          </div>
          <ul class="nav-links">
            <li><a href="index.html">Início</a></li>
            <li><a href="cardapio_comida.html">Cardápio</a></li>
            <li><a href="cardapio_jogos.html" class="active">Jogos</a></li>
          </ul>
        </nav>
      </header>
      
      <main>
        <section class="bem-vindos">
          <div class="container">
            <h1>🎮 Nossos Jogos</h1>
            {{CONTEUDO}}
          </div>
        </section>
      </main>

      <footer>
        <p>&copy; 2024 Luna & Hops Tavern. | Todos os direitos reservados.</p>
      </footer>
    </body>
    </html>"""

    blocos = ""

    for categoria, itens in jogos.items():
        emoji = {
            "tabuleiro": "🎲",
            "maquinas": "🕹️"
        }.get(categoria, "✨")

        blocos += f"<h2>{emoji} {categoria.capitalize()}</h2><div class='cards-grid'>"

        for item in itens:
            imagem = normalize_asset_path(item.get('imagem', ''))
            if imagem:
                blocos += f"""
            <div class="card">
                <img src="{imagem}" alt="{item['nome']}" class="card-image">
                <div class="card-content">
                    <h3>{item['nome']}</h3>
                    <p><strong>Tipo:</strong> {item['tipo']}</p>
                    {f"<p>{item['descricao']}</p>" if item.get('descricao') else ''}
                </div>
            </div>
            """
            else:
                blocos += f"""
            <div class="card">
                <div class="card-content">
                    <h3>{item['nome']}</h3>
                    <p><strong>Tipo:</strong> {item['tipo']}</p>
                    {f"<p>{item['descricao']}</p>" if item.get('descricao') else ''}
                </div>
            </div>
            """
        blocos += "</div>"

    return html.replace("{{CONTEUDO}}", blocos)
