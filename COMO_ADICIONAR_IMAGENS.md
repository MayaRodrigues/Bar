# Como Adicionar Imagens aos Cardápios (Versão Django)

## Visão Geral

As imagens dos modelos (`ItemCardapio` e `Jogo`) são **armazenadas no banco de dados** usando `django-db-file-storage`. Você pode adicioná-las pelo **Django Admin** ou automaticamente a partir do **catálogo pronto** (`catalogo_pronto/`).

## Opções de Adição de Imagens

### 1) Via Django Admin (recomendado para alterações manuais)
- Acesse: http://127.0.0.1:8000/admin/
- Edite um `ItemCardapio` ou `Jogo`.
- No campo `imagem`, clique em "Choose File" e envie.
- Salve.
- Ao substituir/limpar a imagem e salvar, o arquivo antigo é removido do banco automaticamente.

### 2) Popular automaticamente com o catálogo pronto
- Estrutura esperada:
  ```
  catalogo_pronto/
  ├── comidas.json
  ├── jogos.json
  └── images/
      ├── comidas/...
      ├── bebidas/...
      ├── sobremesas/...
      └── jogos/
          ├── tabuleiro/...
          └── maquinas/...
  ```
- Os JSONs referenciam imagens com caminhos `/assets/images/...`.
- O comando mapeia esses caminhos para `catalogo_pronto/images/...` (removendo o prefixo `images/` quando necessário) e anexa aos modelos.
- Execute:
  ```bash
  python manage.py popular_banco
  ```

## Como funciona por baixo dos panos
- `DEFAULT_FILE_STORAGE = 'db_file_storage.storage.DatabaseFileStorage'`
- `ItemCardapio.imagem` e `Jogo.imagem` usam `upload_to` específico (`cardapio.ItemCardapioImage/...` e `cardapio.JogoImage/...`).
- Em `save()` e `delete()`, os hooks removem a imagem antiga do banco quando você substitui/limpa ou exclui o objeto.
- As URLs públicas das imagens aparecem como `/files/get/?name=...` (camada de compatibilidade local).

## Dicas e Boas Práticas
- Formatos: JPG/PNG. Tamanho até ~500KB para bom desempenho.
- Nomenclatura: evite espaços. Ex.: `Pizza_da_Constelacao.png`.
- Para novos itens via JSON: adicione o caminho no JSON e a imagem correspondente em `catalogo_pronto/images/...`.

## Solução de Problemas
- "Imagem não aparece":
  - Confirme que o item possui imagem (Admin) ou que o arquivo existe em `catalogo_pronto/images/...` e que o JSON referencia `/assets/images/...` corretamente.
  - Reexecute `python manage.py popular_banco` (apaga e recria os dados).
- 404 em imagens de layout (logo/slider/fundo): são arquivos estáticos em `cardapio/static/images`; não fazem parte dos modelos.
