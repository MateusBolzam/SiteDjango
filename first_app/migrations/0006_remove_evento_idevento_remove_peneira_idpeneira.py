# Generated by Django 4.2.4 on 2023-10-04 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_evento_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='idEvento',
        ),
        migrations.RemoveField(
            model_name='peneira',
            name='idPeneira',
        ),
    ]
