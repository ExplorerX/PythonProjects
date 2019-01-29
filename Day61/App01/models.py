from django.db import models

# Create your models here.


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True, null=False)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, unique=True, null=False)
    publisher = models.ForeignKey(to="Publisher")


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False)
    book = models.ManyToManyField(to="Book")
