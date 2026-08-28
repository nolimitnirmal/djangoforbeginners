# Django for Beginners

Practice projects and exercises based on *Django for Beginners*. The repository
shows the progression from a basic Python script to Django views, templates,
URL routing, and multi-page websites.

## Project overview

| Directory | Description |
| --- | --- |
| `ch1-setup` | Basic Python “Hello, World!” script |
| `helloworld` | First Django app with a simple HTTP response |
| `company2` | A home page rendered from a template |
| `company` | Home and about pages with template inheritance and context data |
| `personal_website` | Initial personal website project setup |
| `personalwebsite2` | Personal website with home and about routes |

## Requirements

- Python 3.12 or later
- Django
- `uv` or `pip` for dependency management

## Run the latest project

The latest project uses `uv` and has its dependencies recorded in
`personalwebsite2/pyproject.toml`:

```bash
cd personalwebsite2
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Then open <http://127.0.0.1:8000/>. The about page is available at
<http://127.0.0.1:8000/about/>.

## Run an earlier project

Create a virtual environment and install the pinned dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r helloworld/requirements.txt
```

Choose a project containing `manage.py`, then run it. For example:

```bash
cd company
python manage.py migrate
python manage.py runserver
```

## Tests

Run tests from the relevant project directory:

```bash
python manage.py test
```

These projects are intended for local learning and development, not production
deployment.
