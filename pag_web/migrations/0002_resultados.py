# Generated by Django 4.2.5 on 2023-09-19 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pag_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resultados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pag_web.usuario')),
            ],
        ),
    ]