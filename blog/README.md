# Django Blog

A small blog application built with Django. It demonstrates Django models,
class-based views, templates, authentication, and CRUD operations using a local
SQLite database.

## Features

- List all blog posts on the home page
- View an individual post
- Create, edit, and delete posts
- Create an account and log in or out
- Manage posts through the Django admin site
- Run automated model, URL, view, and template tests

> [!NOTE]
> This is a learning project. The create, edit, and delete views are not yet
> restricted to authenticated users or post authors and should not be deployed
> publicly in their current form.

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/) (recommended), or `pip`

The project uses Django 6.1 or newer. Dependency versions are defined in
`pyproject.toml` and locked in `uv.lock`.

## Getting started

Clone the repository, enter the project directory, and install the dependencies:

```bash
uv sync
```

Apply the database migrations:

```bash
uv run python manage.py migrate
```

Start the development server:

```bash
uv run python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

### Using `pip` instead

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install "django>=6.1"
python manage.py migrate
python manage.py runserver
```

On Windows, activate the virtual environment with
`.venv\Scripts\activate`.

## User accounts

Create an account at <http://127.0.0.1:8000/accounts/signup/> or log in at
<http://127.0.0.1:8000/accounts/login/>.

To access the admin site, create a superuser:

```bash
uv run python manage.py createsuperuser
```

Then visit <http://127.0.0.1:8000/admin/>.

## Main routes

| Route | Purpose |
| --- | --- |
| `/` | List all posts |
| `/post/<id>/` | View a post |
| `/post/new/` | Create a post |
| `/post/<id>/edit/` | Edit a post |
| `/post/<id>/delete/` | Delete a post |
| `/accounts/signup/` | Create an account |
| `/accounts/login/` | Log in |
| `/accounts/logout/` | Log out (POST request) |
| `/admin/` | Django administration |

## Running checks and tests

Run Django's system checks:

```bash
uv run python manage.py check
```

Run the test suite:

```bash
uv run python manage.py test
```

## Project structure

```text
blog/
├── accounts/          # Signup view and URL configuration
├── blog/              # Post model, views, URLs, admin, and tests
├── django_project/    # Project settings and root URL configuration
├── static/css/        # Site styles
├── templates/         # Blog and authentication templates
├── manage.py          # Django management command entry point
├── pyproject.toml     # Project metadata and dependencies
└── uv.lock            # Locked dependency versions
```

## Data model

Each `Post` contains a title, body, and author. Deleting a user also deletes
their posts because the author relationship uses `CASCADE`.
