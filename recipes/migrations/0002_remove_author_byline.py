# Generated by Django 3.0.6 on 2020-05-06 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='byline',
        ),
    ]
