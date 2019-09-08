from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    itemlist = models.ForeignKey('Itemlist', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
