# Como Rodar o Projeto - Luna & Hops Tavern

Este projeto agora roda em Django. Para configurar e executar, siga o guia atualizado:

- **Guia completo:** veja [DJANGO_SETUP.md](DJANGO_SETUP.md)
- **Setup automatizado (recomendado no Windows):**
  ```powershell
  ./setup_django.ps1
  ```

Resumo do fluxo atual:
- O script cria/ativa a venv, instala dependências, roda migrações, permite criar superusuário e pergunta se deseja popular o banco com o catálogo pronto de `catalogo_pronto/` (JSON + imagens salvas no banco).
- Inicie o servidor com `python manage.py runserver` e acesse:
  - Site: http://127.0.0.1:8000/
  - Admin: http://127.0.0.1:8000/admin/

Observação:
- A geração estática por scripts (`scripts/site.py`) foi descontinuada e mantida apenas como legado. As páginas agora são geradas dinamicamente via Django.
