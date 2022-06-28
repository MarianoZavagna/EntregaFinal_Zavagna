from django.db import models
from user.models import User

class Discussion(models.Model):
    title = models.CharField('Título', max_length=100, null=True)
    subtitle = models.CharField('Subtítulo', max_length=100, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField('Descripción')
    image = models.ImageField('Imagen', upload_to='image_post', null=True, blank=True)
    date_posted = models.DateField('Fecha de publicación', auto_now_add=True)

    def __str__(self):
        return f'{self.title} ----> por: {self.author.first_name} {self.author.last_name} - {self.date_posted}'


class ImagePost(models.Model):
    user = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image_post', null=True, blank=True)

    def __str__(self):
        return f'url: {self.image.url}'


class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, related_name="comments",on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField('Comentario')
    date_posted = models.DateTimeField('Fecha de publicación', auto_now_add=True)

    def __str__(self):
        return f'{self.author.first_name} {self.author.last_name} - {self.date_posted}'