# Generated by Django 4.2.4 on 2023-10-04 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_peneira_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='nome',
            field=models.CharField(default='evento', max_length=128),
        ),
    ]
