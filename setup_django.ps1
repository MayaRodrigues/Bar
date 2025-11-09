# Script de configuração rápida do Django
# Luna & Hops Tavern

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Luna & Hops Tavern - Setup Django" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se o ambiente virtual está ativo
if (-not $env:VIRTUAL_ENV) {
    Write-Host "Ambiente virtual nao esta ativo!" -ForegroundColor Yellow
    Write-Host "Ativando ambiente virtual..." -ForegroundColor Cyan
    .\venv\Scripts\Activate.ps1
}

Write-Host "Ambiente virtual ativo" -ForegroundColor Green
Write-Host ""

# Instala dependências
Write-Host "Instalando dependencias..." -ForegroundColor Cyan
pip install -r requirements.txt
Write-Host ""

# Executa migrações
Write-Host "Executando migrações do banco de dados..." -ForegroundColor Cyan
python manage.py makemigrations
python manage.py migrate
Write-Host ""

# Pergunta se deseja criar superusuário
Write-Host "Deseja criar um superusuario agora? (S/N)" -ForegroundColor Yellow
$resposta = Read-Host
if ($resposta -eq "S" -or $resposta -eq "s") {
    Write-Host "Criando superusuario..." -ForegroundColor Cyan
    python manage.py createsuperuser
    Write-Host ""
}

# Pergunta se deseja popular o banco
Write-Host "Deseja usar o cardápio pronto (JSON + imagens) para popular o banco? (S/N)" -ForegroundColor Yellow
$resposta = Read-Host
if ($resposta -eq "S" -or $resposta -eq "s") {
    Write-Host "Populando banco de dados com o cardápio pronto (JSON + imagens)..." -ForegroundColor Cyan
    python manage.py popular_banco
    Write-Host ""
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  ✅ Configuração concluida!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para iniciar o servidor, execute:" -ForegroundColor Yellow
Write-Host "python manage.py runserver" -ForegroundColor White
Write-Host ""
Write-Host "URLs importantes:" -ForegroundColor Yellow
Write-Host "  Site: http://127.0.0.1:8000/" -ForegroundColor White
Write-Host "  Admin: http://127.0.0.1:8000/admin/" -ForegroundColor White
Write-Host ""
