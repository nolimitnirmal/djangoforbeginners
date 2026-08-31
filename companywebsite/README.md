# Company Website

A small Django company website with home and about pages. The project demonstrates URL routing, function- and class-based views, template inheritance, context data, and basic view tests.

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/) (recommended) or `pip`

## Getting started

Clone the repository, move into the project directory, and install the dependencies:

```bash
uv sync
```

Apply the database migrations and start the development server:

```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

### Using pip instead of uv

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "Django>=6.1" "black>=26.5.1"
python manage.py migrate
python manage.py runserver
```

On Windows, activate the virtual environment with `.venv\Scripts\activate`.

## Available pages

| URL | Description |
| --- | --- |
| `/` | Company homepage and sample inventory |
| `/about/` | Company contact information |
| `/admin/` | Django administration site |

## Running tests

```bash
uv run python manage.py test
```

## Code formatting

Format the Python source with Black:

```bash
uv run black .
```

## Project structure

```text
companywebsite/
├── django_project/   # Project settings and root URL configuration
├── pages/            # Home and about views, URLs, and tests
├── templates/        # Shared and page-specific HTML templates
├── manage.py         # Django command-line utility
├── pyproject.toml    # Project metadata and dependencies
└── uv.lock           # Locked dependency versions
```

## Development note

The current settings are intended for local development. Before deploying, move the secret key into an environment variable, disable debug mode, configure allowed hosts, and use a production-ready server and static-file setup.
