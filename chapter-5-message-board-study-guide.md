# Chapter 5 Study Guide: Message Board Website

This study guide covers the beginner-level knowledge introduced in Chapter 5 of *Django for Beginners, 5th Edition*. The chapter builds a database-backed message board and connects these pieces:

```text
Database -> Model -> Migration -> ORM query -> View -> Template
```

## Databases and Django's ORM

### 1. What is a relational database?

A relational database stores information in tables made of columns and rows. Separate tables can also be related to one another.

### 2. In a database table, what are rows and columns?

- **Columns** define the kinds of information the table can store.
- **Rows** contain the actual data.

For the message board, `text` is a column and each saved message is a row.

### 3. What does CRUD stand for?

CRUD stands for:

- **Create** data
- **Read** data
- **Update** data
- **Delete** data

These are the basic operations performed on database data.

### 4. What does ORM stand for?

ORM stands for **Object-Relational Mapper**.

### 5. What does Django's ORM allow us to do?

Django's ORM lets us define database models and work with database data using Python instead of writing raw SQL ourselves.

## Models and Migrations

### 6. What is a Django model?

A Django model is a Python class that describes the structure of data in the database. A model class represents a database table, and its fields represent the table's columns.

### 7. In this code, what does `Post` represent?

```python
class Post(models.Model):
    text = models.TextField()
```

`Post` is the model class. It represents the database table used to store message board posts. Each `Post` object represents one row in that table.

### 8. What does `text = models.TextField()` represent?

It creates a model field named `text`. This becomes a database column that stores the text content of each post. `TextField()` tells Django that the value will be text.

### 9. What is the purpose of `makemigrations`?

`makemigrations` creates a migration file that records changes made to the models.

```shell
python manage.py makemigrations posts
```

The migration file gives Django instructions for changing the database structure.

### 10. What is the purpose of `migrate`?

`migrate` executes the instructions in migration files and applies those changes to the database.

```shell
python manage.py migrate
```

### 11. What is the correct order: `migrate` first or `makemigrations` first?

After creating or changing a model, run `makemigrations` first and `migrate` second:

```text
Change models.py
      -> makemigrations
      -> migration file
      -> migrate
      -> database updated
```

## Django Admin

### 12. What is Django's admin site used for?

The admin site is a built-in interface for managing project data. In this chapter, it is used to create, view, edit, and delete message board posts without writing code for those actions.

### 13. What does `python manage.py createsuperuser` do?

It creates a superuser account that can log in to Django's admin site.

```shell
python manage.py createsuperuser
```

The command asks for a username, email, and password.

### 14. Why do we write `admin.site.register(Post)`?

We register `Post` so that the model appears in the admin site and its data can be managed there.

```python
from django.contrib import admin

from .models import Post

admin.site.register(Post)
```

### 15. What is the purpose of a model's `__str__()` method?

`__str__()` provides a readable description of a model object. Without it, Django may display a label such as `Post object (1)`.

```python
def __str__(self):
    return self.text[:50]
```

This version displays the first 50 characters of the post. It changes how the object is shown, not the stored post text.

## Querying the Database

### 16. What does this query do?

```python
Post.objects.all()
```

It asks the database for all saved `Post` objects.

### 17. What is `Post` in that query?

`Post` is the model class. It represents the database table being queried.

### 18. What is `objects`?

`objects` is the default manager Django adds to a model. A manager provides methods for interacting with the database and performing queries.

### 19. What does `all()` return?

`all()` returns all instances of the `Post` model from the database in a QuerySet.

### 20. What is a QuerySet?

A QuerySet is the result of a database query that retrieves a collection of objects. Here, it contains the `Post` objects returned by the query.

## Function-Based View and Template

### 21. In this function-based view, where is the database queried?

```python
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})
```

The database is queried on this line:

```python
posts = Post.objects.all()
```

The returned QuerySet is stored in the `posts` variable.

### 22. What is the purpose of the context dictionary `{"posts": posts}`?

The context dictionary passes data from the view to the template. The key `"posts"` becomes the name the template can use, and its value is the `posts` QuerySet.

### 23. How does this template display every Post?

```django
{% for post in posts %}
    <li>{{ post.text }}</li>
{% endfor %}
```

The `{% for %}` template tag loops through the `posts` collection. During each loop, `post` refers to one `Post` object, and an HTML list item displays its text.

### 24. What does `{{ post.text }}` display?

It displays the value stored in the current `Post` object's `text` field.

## URLs and Class-Based Views

### 25. What does `include("posts.urls")` do?

It tells the project-level URL configuration to pass matching URL requests to the URL patterns in the `posts` app.

```python
path("", include("posts.urls"))
```

In this chapter, a request for the homepage is passed to `posts/urls.py`.

### 26. What is `ListView` used for?

`ListView` is a built-in generic class-based view for displaying a list of objects from a database model.

### 27. In this class-based view, what do `model` and `template_name` tell Django?

```python
class PostList(ListView):
    model = Post
    template_name = "post_list.html"
```

- `model = Post` tells Django which model's objects to list.
- `template_name = "post_list.html"` tells Django which template to render.

By default, this `ListView` provides the template with a context variable named `post_list`.

### 28. Why do we use `.as_view()` here?

```python
path("", PostList.as_view(), name="home")
```

The URL system needs a callable view. `.as_view()` turns the `PostList` class into a callable view that Django can use when a request reaches this URL.

### 29. What is the main difference between the function-based `post_list` view and the `PostList` class-based view?

The function-based view explicitly performs the query, builds the context dictionary, and calls `render()`. The class-based `PostList` view inherits common list-display behavior from Django's `ListView`; we only specify the model and template.

Both approaches display the posts. The chapter says choosing between a function-based view and a generic class-based view is a matter of preference.

## Tests

### 30. Why does this chapter use `TestCase` instead of `SimpleTestCase`?

This project works with a database. `TestCase` lets the tests create and use a separate test database, while `SimpleTestCase` is for tests that do not need database access.

Using a separate test database is safer than running tests against the real project database. Django destroys the test database when the tests finish.

### 31. What is the purpose of `setUpTestData()`?

`setUpTestData()` creates test data once for the test case so that later test methods can use it.

```python
@classmethod
def setUpTestData(cls):
    cls.post = Post.objects.create(text="This is a test!")
```

Here it creates a test `Post`. The chapter explains that this is faster than creating the data before every test with `setUp()`.

### 32. What does `self.client.get("/")` do in a Django test?

It uses Django's test client to simulate a GET request to the homepage at `/`. The returned response is stored so the test can inspect it.

```python
response = self.client.get("/")
```

### 33. What does status code `200` tell us?

An HTTP status code of `200` means the request succeeded. In this test, it confirms that the homepage exists and returned a successful response.

```python
self.assertEqual(response.status_code, 200)
```

### 34. What does `reverse("home")` give us?

`reverse("home")` looks up the URL whose pattern has `name="home"` and returns that URL. In this project, it returns the homepage URL.

```python
response = self.client.get(reverse("home"))
```

### 35. What does `assertTemplateUsed()` check?

It checks that Django used the expected template to produce the response.

```python
self.assertTemplateUsed(response, "post_list.html")
```

### 36. What does `assertContains()` check?

It checks that the response contains the expected content.

```python
self.assertContains(response, "This is a test!")
```

In this chapter, it confirms that the post created in the test database appears on the homepage.

## Chapter 5 Big Picture

When someone visits the message board homepage, the pieces work together like this:

```text
Browser requests /
        -> URL pattern selects PostList
        -> ListView queries the Post model
        -> Django's ORM reads the database
        -> Posts are passed to post_list.html
        -> The template loops over the posts
        -> Django returns the rendered HTML
```

If you can explain that flow and the two-step migration process, you understand the main lesson of Chapter 5.
