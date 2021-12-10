# Pet share HackYeah 2021

## How to install

1. Download repo
2. Initialize virtual environment in it: `python -m venv venv`
3. Run that venv: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy pyvenv.example.cnf to pyvenv.cnf and fill in credentials
6. Migrate database: `python manage.py migrate`
7. Seed data: `python manage.py loaddata seed.json`
8. To run dev server: `python manage.py runserver`