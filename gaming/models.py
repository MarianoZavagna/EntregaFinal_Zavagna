from django.db import models


class Gaming(models.Model):
    name = models.CharField(max_length=40)
    platform = models.CharField(max_length=40)
    description = models.TextField(blank = True, null=True)


    def __str__(self):
        return f'{self.name} gaming --'