# Generated by Django 5.2 on 2025-04-27 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Market.musician')),
            ],
        ),
    ]
