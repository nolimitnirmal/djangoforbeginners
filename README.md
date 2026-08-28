# Django for Beginners

A collection of small projects and exercises created while learning Django.

## Projects

- `ch1-setup` – a basic Python “Hello, World!” example
- `helloworld` – a minimal Django app that returns a text response
- `company2` – a simple template-based home page
- `company` – home and about pages using Django views and templates
- `personal_website` – a starter Django project

## Getting started

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r helloworld/requirements.txt
   ```

3. Choose a project and start its development server. For example:

   ```bash
   cd company
   python manage.py migrate
   python manage.py runserver
   ```

4. Open <http://127.0.0.1:8000/> in your browser.

## Running tests

From a Django project directory, run:

```bash
python manage.py test
```
