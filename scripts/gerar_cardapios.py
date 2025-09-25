import json
import os

def gerar_cardapio(arquivo_json, template_html, saida_html):
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)

    cardapio = dados["cardapio"]

    with open(template_html, "r", encoding="utf-8") as f:
        html = f.read()

    blocos = ""

    for categoria, itens in cardapio.items():
        emoji = {
            "comidas": "🍽️",
            "bebidas": "🍹",
            "sobremesas": "🍰",
            "porcoes": "🧙‍♂️"
        }.get(categoria, "✨")

        blocos += f"<h2>{emoji} {categoria.capitalize()}</h2><div class='container'>"

        for item in itens:
            blocos += f"""
            <div class="card">
                <h3>{item['nome']}</h3>
                <p>{item['descricao']}</p>
            </div>
            """
        blocos += "</div>"

    html = html.replace("{{CONTEUDO}}", blocos)

    with open(saida_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Cardápio gerado em {saida_html}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "..", "data")
    site_dir = os.path.join(base_dir, "..", "site")

    gerar_cardapio(
        arquivo_json=os.path.join(data_dir, "cardapio.json"),
        template_html=os.path.join(site_dir, "template_cardapio.html"),
        saida_html=os.path.join(site_dir, "cardapio.html")  
    )

    def gerar_cardapio_jogos(arquivo_json, template_html, saida_html):
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)

    jogos = dados["jogos"]

    with open(template_html, "r", encoding="utf-8") as f:
        html = f.read()

    blocos = ""

    # Percorre categorias de jogos (tabuleiro, máquinas, etc.)
    for categoria, itens in jogos.items():
        emoji = {
            "tabuleiro": "🎲",
            "maquinas": "🕹️"
        }.get(categoria, "✨")

        blocos += f"<h2>{emoji} {categoria.capitalize()}</h2><div class='container'>"

        for item in itens:
            blocos += f"""
            <div class="card">
                <h3>{item['nome']}</h3>
                <p><strong>Tipo:</strong> {item['tipo']}</p>
            </div>
            """
        blocos += "</div>"

    html = html.replace("{{CONTEUDO}}", blocos)

    with open(saida_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Lista de jogos gerada em {saida_html}")
