# Como Rodar o Projeto - Luna & Hops Tavern

## Requisitos

- Python 3.10 ou superior
- Sistema operacional: Windows, macOS ou Linux
- Navegador web instalado (para visualizar os HTMLs gerados)

Bibliotecas Python externas: nenhuma. O projeto usa apenas a biblioteca padrão do Python (os, sys, json, webbrowser, typing).

## Estrutura Importante

- `data/` contém os arquivos JSON de entrada (`comidas.json`, `jogos.json`).
- `scripts/site.py` é o script principal (modo interativo e linha de comando).
- `scripts/gerar_html.py` gera os HTMLs a partir dos JSONs.
- `scripts/gerar_css.py` cria `site/style.css` apenas se ele não existir.
- `site/` contém os arquivos HTML e CSS do site.
- `assets/` contém as imagens e vídeos usados no site.

## Execução (Modo Interativo)

1. Abra um terminal no diretório `scripts/`.
2. Execute:
   ```bash
   python site.py
   ```
3. Escolha uma opção no menu:
   - Digitar um arquivo JSON (ex.: `../data/comidas.json`)
   - Digitar um diretório com JSONs (ex.: `../data`)
   - Digitar `todos` para gerar tudo
   - Digitar `sair` para encerrar

Ao final, o programa abrirá `site/index.html` (ou os cardápios) no navegador.

## Execução (Linha de Comando)

- Gerar um cardápio específico:
  ```bash
  python site.py ../data/comidas.json
  ```
- Processar todos os arquivos JSON de um diretório:
  ```bash
  python site.py ../data
  ```
- Usar caminho absoluto:
  ```bash
  python site.py "C:\Users\seuusuario\Documents\Bar\data\jogos.json"
  ```

## Notas sobre Imagens

- Nos JSONs, caminhos aceitos para imagens: `../assets/...`, `/assets/...` ou `assets/...`.
- Caminhos que começarem com `/assets/...` ou `assets/...` serão normalizados automaticamente para `../assets/...` ao gerar as páginas dentro de `site/`.
- Se as imagens não aparecerem, verifique se os arquivos realmente existem sob `assets/images/...` e se a estrutura de pastas corresponde ao caminho usado.

## Problemas Comuns

- "Arquivo não encontrado": confirme o caminho digitado e a existência do arquivo.
- "JSON inválido": valide o conteúdo com um validador JSON e corrija vírgulas e chaves.
- Nada abre no navegador: verifique se `site/index.html` existe; o script abre os cardápios como fallback.

## Desenvolvimento

- O CSS padrão está em `site/style.css`. Se ausente, `scripts/gerar_css.py` criará um novo baseado em `DEFAULT_STYLE_CSS`.
- A geração de HTML é feita por `scripts/gerar_html.py`, nas funções `gerar_cardapio_comida()` e `gerar_cardapio_jogos()`.
- Para ajustar dimensões de cards/imagens, edite as classes `.card`, `.card-image`, `.cards-grid` em `site/style.css`.
