from django.db import models


class Hardware(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=40)
    description = models.TextField(blank = True, null=True)


    def __str__(self):
        return f'{self.name} Hardware --'