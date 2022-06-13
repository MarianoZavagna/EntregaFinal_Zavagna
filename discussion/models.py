from django.db import models


class Discussion(models.Model):
    title = models.CharField(max_length=100, null=True)
    platform = models.CharField(max_length=100, null=True)
    description = models.TextField()
    

    def __str__(self):
        return f'{self.title} Discussion --'