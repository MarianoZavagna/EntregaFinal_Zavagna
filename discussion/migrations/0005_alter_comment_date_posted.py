# Generated by Django 4.0.5 on 2022-06-19 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0004_alter_comment_discussion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicación'),
        ),
    ]
