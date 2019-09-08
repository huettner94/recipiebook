from django.db import models

class Itemlist(models.Model):
    name = models.CharField(max_length=100)
    recipie = models.ForeignKey('Recipie', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
