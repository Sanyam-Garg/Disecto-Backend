from django.db import models

# Create your models here.
class List(models.Model):
    """
    Model for each list produced or wanted
        items --> ManyToMany relation since one list can have multiple items and one item can be a part of multiple lists
    """
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Item(models.Model):
    """
    Model for all the items in the database.
        stock --> The available quantity of the item
    """
    name = models.CharField(max_length=100, unique=True)
    stock = models.IntegerField(default=100)
    price = models.IntegerField(default=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name