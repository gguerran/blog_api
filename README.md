# Blog API

API para gerenciamento de Posts

## Documentação

A documentação para uso desta API se encontra no arquivo DOC.md

## Como desenvolver?

1. Clone do  repositório.
2. Crie um virtualenv com Python 3
3. Ative o virtualenv.
4. Instale as dependências.
5. Acesse o banco
6. Crie o banco de dados
7. Crie o usuario como super usuário com a senha TQd03YI2z^YF
8. Execute as migrations
9. Execute os testes.
10. Execute a aplicação

```console
git clone https://github.com/gguerran/blog_api.git
cd blog_api
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
sudo su - postgres
createdb blog_db
createuser -P -s -i -d -r -l -w blog_user # Password -> TQd03YI2z^YF
exit
python manage.py migrate
python manage.py test
python manage.py runserver
```
