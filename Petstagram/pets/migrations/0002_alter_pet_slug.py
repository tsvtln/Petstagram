# Generated by Django 5.0.4 on 2024-10-13 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]