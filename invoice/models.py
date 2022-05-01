from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=100)
    price = models.IntegerField(default=100)

    def __str__(self):
        return self.name

class List(models.Model):
    title = models.CharField(max_length=200)
    items = models.ManyToManyField(Item, related_name='item_lists')

    def __str__(self):
        return self.title