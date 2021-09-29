from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import TextField
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()


class Post(models.Models):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    # db_index let Django and SQL trade a index for that field to make querying and filtering based on it a bit more effective.
    # db_index=True is default.
    slug = models.SlugField(unique=True, db_index=True)
    content = TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts")