# Clube de Programação — Sistema Administrativo (esboço)

Este repositório contém um scaffold inicial em Django para o sistema "Clube de Programação".

Passos rápidos para rodar localmente (Windows):

1. Criar e ativar ambiente virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Instalar dependências:

```powershell
pip install -r requirements.txt
```

3. Migrar banco e criar superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Rodar servidor:

```powershell
python manage.py runserver
```

Abra http://127.0.0.1:8000/ para ver a página pública e /admin/ para acessar o painel administrativo.

Explicações e próximos passos podem ser fornecidos passo a passo.
