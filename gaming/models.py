from django.db import models


class Gaming(models.Model):
    name = models.CharField('Nombre',max_length=40)
    platform = models.CharField('Plataforma', max_length=40)
    description = models.TextField('Descripción', blank = True, null=True)


    def __str__(self):
        return f'{self.name} {self.platform}'