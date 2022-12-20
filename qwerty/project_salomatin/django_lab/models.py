from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

class Films(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    release_date = models.DateField()
    actors = models.CharField(max_length=30)
    show_date = models.DateField()