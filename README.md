# SOAP maths project

An example of service soap using django, spyne, lxml and suds-py3.

## Tech stack

- Python 3
- Django
- Spyne (SOAP)
- lxml
- suds (SOAP client)
- Database: SQLite

## Project structure

- `soap_maths_project/`: project settings and root URLs
- `maths_app/`: Django app
- Tests: `maths_app/tests.py`

## URL routes

Declared in `urls.py`:

- `/blog/`
- `/maths/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
