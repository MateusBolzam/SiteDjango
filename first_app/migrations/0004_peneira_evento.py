# Generated by Django 4.2.4 on 2023-10-04 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_personagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peneira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPeneira', models.IntegerField(unique=True)),
                ('temperature', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEvento', models.IntegerField(unique=True)),
                ('create', models.DateField()),
                ('temperature', models.IntegerField()),
                ('idPeneira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.peneira')),
            ],
        ),
    ]