# Blog API

API para gerenciamento de Posts

## Como desenvolver?

1. Clone do  repositório.
2. Crie um virtualenv com Python 3
3. Ative o virtualenv.
4. Instale as dependências.
5. Execute os testes.
6. Execute as migrations
7. Execute a aplicação

```console
git clone #
cd blog_api
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py test
python manage.py migrate
python manage.py runserver
```