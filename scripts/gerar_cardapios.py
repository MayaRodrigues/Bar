import json
import os
import sys
import webbrowser
from pathlib import Path

def gerar_cardapio_comida(arquivo_json, saida_html):
    """Gera o cardápio de comidas a partir de um arquivo JSON"""
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)

    cardapio = dados["cardapio"]

    # Template HTML embutido
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
        <img src="/assets/images/logo.png" alt="Logo do Bar de Jogos">
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
            # Verifica se o item tem imagem
            imagem = item.get('imagem', '')
            
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

    html = html.replace("{{CONTEUDO}}", blocos)

    with open(saida_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Cardápio gerado em {saida_html}")
    return saida_html


def gerar_cardapio_jogos(arquivo_json, saida_html):
    """Gera o cardápio de jogos a partir de um arquivo JSON"""
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)

    jogos = dados["jogos"]

    # Template HTML embutido
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
        <img src="/assets/images/logo.png" alt="Logo do Bar de Jogos">
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
            # Verifica se o item tem imagem
            imagem = item.get('imagem', '')
            
            if imagem:
                blocos += f"""
            <div class="card">
                <img src="{imagem}" alt="{item['nome']}" class="card-image">
                <div class="card-content">
                    <h3>{item['nome']}</h3>
                    <p><strong>Tipo:</strong> {item['tipo']}</p>
                </div>
            </div>
            """
            else:
                blocos += f"""
            <div class="card">
                <div class="card-content">
                    <h3>{item['nome']}</h3>
                    <p><strong>Tipo:</strong> {item['tipo']}</p>
                </div>
            </div>
            """
        blocos += "</div>"

    html = html.replace("{{CONTEUDO}}", blocos)

    with open(saida_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Lista de jogos gerada em {saida_html}")
    return saida_html


def detectar_tipo_json(arquivo_json):
    """Detecta se o JSON contém dados de comida ou jogos"""
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)
    
    if "cardapio" in dados:
        return "comida"
    elif "jogos" in dados:
        return "jogos"
    else:
        raise ValueError("Formato de JSON não reconhecido. Deve conter 'cardapio' ou 'jogos'")


def processar_caminho(caminho, site_dir):
    """Processa um arquivo ou diretório e gera os cardápios"""
    if os.path.isfile(caminho):
        # É um arquivo JSON específico
        if not caminho.endswith('.json'):
            print(f"❌ Erro: '{caminho}' não é um arquivo JSON válido")
            return False
        
        try:
            tipo = detectar_tipo_json(caminho)
            
            if tipo == "comida":
                saida = os.path.join(site_dir, "cardapio_comida.html")
                html_gerado = gerar_cardapio_comida(caminho, saida)
            else:
                saida = os.path.join(site_dir, "cardapio_jogos.html")
                html_gerado = gerar_cardapio_jogos(caminho, saida)
            
            # Abre o arquivo no navegador
            print("\n🌐 Abrindo cardápio no navegador...")
            webbrowser.open('file://' + os.path.abspath(html_gerado))
            return True
            
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"❌ Erro ao processar o arquivo JSON: {e}")
            return False
            
    elif os.path.isdir(caminho):
        # É um diretório, processa todos os JSONs dentro dele
        print(f"📁 Processando arquivos no diretório: {caminho}")
        
        arquivos_json = [f for f in os.listdir(caminho) if f.endswith('.json')]
        
        if not arquivos_json:
            print(f"❌ Erro: Nenhum arquivo JSON encontrado no diretório '{caminho}'")
            return False
        
        try:
            for arquivo in arquivos_json:
                caminho_completo = os.path.join(caminho, arquivo)
                tipo = detectar_tipo_json(caminho_completo)
                
                if tipo == "comida":
                    saida = os.path.join(site_dir, "cardapio_comida.html")
                    gerar_cardapio_comida(caminho_completo, saida)
                else:
                    saida = os.path.join(site_dir, "cardapio_jogos.html")
                    gerar_cardapio_jogos(caminho_completo, saida)
            
            # Abre os arquivos gerados
            print("\n🌐 Abrindo cardápios no navegador...")
            html_comidas = os.path.join(site_dir, "cardapio_comida.html")
            html_jogos = os.path.join(site_dir, "cardapio_jogos.html")
            
            if os.path.exists(html_comidas):
                webbrowser.open('file://' + os.path.abspath(html_comidas))
            if os.path.exists(html_jogos):
                webbrowser.open('file://' + os.path.abspath(html_jogos))
            return True
            
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"❌ Erro ao processar arquivos JSON: {e}")
            return False
    else:
        print(f"❌ Erro: '{caminho}' não existe ou não é um arquivo/diretório válido")
        return False


def solicitar_entrada_usuario(base_dir, data_dir):
    """Solicita entrada do usuário de forma interativa"""
    print("\n" + "="*60)
    print("🍺 Gerador de Cardápios - Luna & Hops Tavern 🎲")
    print("="*60)
    print("\nOpções disponíveis:")
    print("  1. Digite o caminho para um arquivo JSON")
    print("  2. Digite o caminho para um diretório contendo arquivos JSON")
    print("  3. Digite 'todos' para gerar todos os cardápios padrão")
    print("  4. Digite 'sair' para encerrar o programa")
    print("\nExemplos:")
    print(f"  - {os.path.join(data_dir, 'comidas.json')}")
    print(f"  - {data_dir}")
    print("  - todos")
    print("="*60)
    
    while True:
        try:
            entrada = input("\n📝 Digite sua escolha: ").strip()
            
            if not entrada:
                print("⚠️  Entrada vazia. Por favor, digite algo válido.")
                continue
            
            if entrada.lower() == 'sair':
                print("\n👋 Encerrando o programa. Até logo!")
                sys.exit(0)
            
            if entrada.lower() == 'todos':
                return None  # Sinal para gerar todos os cardápios
            
            # Tenta resolver caminhos relativos
            if not os.path.isabs(entrada):
                # Tenta relativo ao diretório base
                caminho_tentativa = os.path.join(base_dir, entrada)
                if os.path.exists(caminho_tentativa):
                    return caminho_tentativa
                
                # Tenta relativo ao diretório data
                caminho_tentativa = os.path.join(data_dir, entrada)
                if os.path.exists(caminho_tentativa):
                    return caminho_tentativa
                
                # Tenta o caminho como está
                if os.path.exists(entrada):
                    return entrada
                
                print(f"⚠️  Caminho '{entrada}' não encontrado.")
                print("💡 Dica: Verifique se o caminho está correto ou use 'todos' para gerar todos os cardápios.")
                continue
            else:
                if os.path.exists(entrada):
                    return entrada
                else:
                    print(f"⚠️  Caminho '{entrada}' não encontrado.")
                    continue
                    
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário. Até logo!")
            sys.exit(0)
        except Exception as e:
            print(f"⚠️  Erro inesperado: {e}")
            print("Por favor, tente novamente.")
            continue


def main():
    """Função principal que processa argumentos da linha de comando"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "..", "data")
    site_dir = os.path.join(base_dir, "..", "site")
    
    # Se nenhum argumento for fornecido, solicita entrada do usuário
    if len(sys.argv) == 1:
        # Loop infinito para permitir múltiplas tentativas
        while True:
            caminho = solicitar_entrada_usuario(base_dir, data_dir)
            
            # Se retornou None, gera todos os cardápios
            if caminho is None:
                print("\n📋 Gerando todos os cardápios...")
                
                try:
                    # Gera cardápio de comidas
                    arquivo_comidas = os.path.join(data_dir, "comidas.json")
                    saida_comidas = os.path.join(site_dir, "cardapio_comida.html")
                    html_comidas = gerar_cardapio_comida(arquivo_comidas, saida_comidas)
                    
                    # Gera cardápio de jogos
                    arquivo_jogos = os.path.join(data_dir, "jogos.json")
                    saida_jogos = os.path.join(site_dir, "cardapio_jogos.html")
                    html_jogos = gerar_cardapio_jogos(arquivo_jogos, saida_jogos)
                    
                    # Abre ambos os arquivos no navegador
                    print("\n🌐 Abrindo cardápios no navegador...")
                    webbrowser.open('file://' + os.path.abspath(html_comidas))
                    webbrowser.open('file://' + os.path.abspath(html_jogos))
                    
                    print("\n✅ Todos os cardápios foram gerados com sucesso!")
                    break  # Sai do loop após sucesso
                    
                except Exception as e:
                    print(f"\n❌ Erro ao gerar cardápios: {e}")
                    print("Por favor, verifique se os arquivos JSON existem no diretório 'data'.")
                    
                    # Pergunta se deseja tentar novamente
                    resposta = input("\n🔄 Deseja tentar novamente? (s/n): ").strip().lower()
                    if resposta not in ['s', 'sim', 'y', 'yes']:
                        print("\n👋 Encerrando o programa. Até logo!")
                        break
                    continue
            else:
                # Processa o caminho fornecido pelo usuário
                sucesso = processar_caminho(caminho, site_dir)
                
                if sucesso:
                    print("\n✅ Cardápio gerado com sucesso!")
                    break  # Sai do loop após sucesso
                else:
                    print("\n⚠️  Falha ao processar o arquivo/diretório.")
                    
                    # Pergunta se deseja tentar novamente
                    resposta = input("\n🔄 Deseja tentar novamente? (s/n): ").strip().lower()
                    if resposta not in ['s', 'sim', 'y', 'yes']:
                        print("\n👋 Encerrando o programa. Até logo!")
                        break
                    continue
        
    else:
        # Processa o arquivo ou diretório fornecido via linha de comando
        caminho = sys.argv[1]
        sucesso = processar_caminho(caminho, site_dir)
        
        if not sucesso:
            print("\n❌ Falha ao processar o arquivo/diretório fornecido.")
            sys.exit(1)
        else:
            print("\n✅ Cardápio gerado com sucesso!")


if __name__ == "__main__":
    main()
