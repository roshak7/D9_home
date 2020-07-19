from django.db import models


class Author(models.Model):
    name = models.Charfield(max_length=255)


class Book(models.Model):
    title = models.Charfield(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)