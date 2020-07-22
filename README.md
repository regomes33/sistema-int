## Como contribuir?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/regomes33/sistema-int.git
cd sistema-int
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/dev.txt # ou
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py create_data
```

### Variáveis de ambiente

Defina suas variáveis de ambiente em `.env`

```
DEBUG=True
SECRET_KEY=...
ALLOWED_HOSTS=127.0.0.1,.localhost
ENDPOINT=http://localhost:8000/
...
```
