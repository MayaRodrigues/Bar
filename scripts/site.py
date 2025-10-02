import os
import sys
import json
import webbrowser
from typing import Optional

from gerar_css import ensure_style_css
from gerar_html import gerar_cardapio_comida, gerar_cardapio_jogos


def detectar_tipo_json(arquivo_json: str) -> str:
    """Detecta se o JSON contém dados de comida ou jogos."""
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)
    if "cardapio" in dados:
        return "comida"
    if "jogos" in dados:
        return "jogos"
    raise ValueError("Formato de JSON não reconhecido. Deve conter 'cardapio' ou 'jogos'")


def gerar_e_salvar_html(arquivo_json: str, saida_html: str) -> str:
    """Carrega o JSON, gera o HTML adequado e salva no caminho de saída."""
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)

    tipo = "comida" if "cardapio" in dados else ("jogos" if "jogos" in dados else None)
    if tipo is None:
        raise ValueError("JSON inválido: esperado 'cardapio' ou 'jogos'")

    html = gerar_cardapio_comida(dados) if tipo == "comida" else gerar_cardapio_jogos(dados)

    site_dir = os.path.dirname(saida_html)
    ensure_style_css(os.path.join(site_dir, "style.css"))

    with open(saida_html, "w", encoding="utf-8") as f:
        f.write(html)

    return saida_html


def processar_caminho(caminho: str, site_dir: str) -> bool:
    """Processa um arquivo ou diretório e gera os cardápios."""
    if os.path.isfile(caminho):
        if not caminho.endswith('.json'):
            print(f"❌ Erro: '{caminho}' não é um arquivo JSON válido")
            return False
        try:
            tipo = detectar_tipo_json(caminho)
            saida = os.path.join(site_dir, "cardapio_comida.html" if tipo == "comida" else "cardapio_jogos.html")
            html_gerado = gerar_e_salvar_html(caminho, saida)
            print("\n🌐 Abrindo cardápio no navegador...")
            webbrowser.open('file://' + os.path.abspath(html_gerado))
            return True
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"❌ Erro ao processar o arquivo JSON: {e}")
            return False

    if os.path.isdir(caminho):
        print(f"📁 Processando arquivos no diretório: {caminho}")
        arquivos_json = [f for f in os.listdir(caminho) if f.endswith('.json')]
        if not arquivos_json:
            print(f"❌ Erro: Nenhum arquivo JSON encontrado no diretório '{caminho}'")
            return False
        try:
            for arquivo in arquivos_json:
                caminho_completo = os.path.join(caminho, arquivo)
                tipo = detectar_tipo_json(caminho_completo)
                saida = os.path.join(site_dir, "cardapio_comida.html" if tipo == "comida" else "cardapio_jogos.html")
                gerar_e_salvar_html(caminho_completo, saida)

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

    print(f"❌ Erro: '{caminho}' não existe ou não é um arquivo/diretório válido")
    return False


def solicitar_entrada_usuario(base_dir: str, data_dir: str) -> Optional[str]:
    """Solicita entrada do usuário de forma interativa."""
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
                return None
            if not os.path.isabs(entrada):
                caminho_tentativa = os.path.join(base_dir, entrada)
                if os.path.exists(caminho_tentativa):
                    return caminho_tentativa
                caminho_tentativa = os.path.join(data_dir, entrada)
                if os.path.exists(caminho_tentativa):
                    return caminho_tentativa
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


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "..", "data")
    site_dir = os.path.join(base_dir, "..", "site")

    if len(sys.argv) == 1:
        while True:
            caminho = solicitar_entrada_usuario(base_dir, data_dir)
            if caminho is None:
                print("\n📋 Gerando todos os cardápios...")
                try:
                    arquivo_comidas = os.path.join(data_dir, "comidas.json")
                    saida_comidas = os.path.join(site_dir, "cardapio_comida.html")
                    html_comidas = gerar_e_salvar_html(arquivo_comidas, saida_comidas)

                    arquivo_jogos = os.path.join(data_dir, "jogos.json")
                    saida_jogos = os.path.join(site_dir, "cardapio_jogos.html")
                    html_jogos = gerar_e_salvar_html(arquivo_jogos, saida_jogos)

                    # Abre a página inicial do site
                    index_path = os.path.join(site_dir, "index.html")
                    if os.path.exists(index_path):
                        print("\n🌐 Abrindo o site no navegador (index.html)...")
                        webbrowser.open('file://' + os.path.abspath(index_path))
                    else:
                        # Fallback: se não houver index.html, abre os cardápios gerados
                        print("\nℹ️  'index.html' não encontrado. Abrindo cardápios gerados no navegador...")
                        webbrowser.open('file://' + os.path.abspath(html_comidas))
                        webbrowser.open('file://' + os.path.abspath(html_jogos))

                    print("\n✅ Todos os cardápios foram gerados com sucesso!")
                    break
                except Exception as e:
                    print(f"\n❌ Erro ao gerar cardápios: {e}")
                    print("Por favor, verifique se os arquivos JSON existem no diretório 'data'.")
                    resposta = input("\n🔄 Deseja tentar novamente? (s/n): ").strip().lower()
                    if resposta not in ['s', 'sim', 'y', 'yes']:
                        print("\n👋 Encerrando o programa. Até logo!")
                        break
                    continue
            else:
                sucesso = processar_caminho(caminho, site_dir)
                if sucesso:
                    print("\n✅ Cardápio gerado com sucesso!")
                    break
                else:
                    print("\n⚠️  Falha ao processar o arquivo/diretório.")
                    resposta = input("\n🔄 Deseja tentar novamente? (s/n): ").strip().lower()
                    if resposta not in ['s', 'sim', 'y', 'yes']:
                        print("\n👋 Encerrando o programa. Até logo!")
                        break
                    continue
    else:
        caminho = sys.argv[1]
        sucesso = processar_caminho(caminho, site_dir)
        if not sucesso:
            print("\n❌ Falha ao processar o arquivo/diretório fornecido.")
            sys.exit(1)
        else:
            print("\n✅ Cardápio gerado com sucesso!")


if __name__ == "__main__":
    main()
