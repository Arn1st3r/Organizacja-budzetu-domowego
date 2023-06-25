# Generated by Django 3.2.19 on 2023-06-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budzet_domowy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lista_lat1',
            fields=[
                ('rok', models.CharField(max_length=4, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Rok',
            },
        ),
        migrations.CreateModel(
            name='lista_miesiecy1',
            fields=[
                ('miesiac', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Miesiąc',
            },
        ),
        migrations.AlterField(
            model_name='cele',
            name='nazwa',
            field=models.CharField(max_length=200),
        ),
    ]
