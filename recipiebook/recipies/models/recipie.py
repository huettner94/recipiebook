from django.db import models


class Recipie(models.Model):
    name = models.CharField(max_length=1000)
    amount = models.PositiveSmallIntegerField(blank=True, null=True,
                                              verbose_name="Personen")

    def __str__(self):
        return self.name
