# Generated by Django 5.0.4 on 2024-10-21 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('photos', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-datetime_of_publication']},
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['datetime_of_publication'], name='common_comm_datetim_0ce93a_idx'),
        ),
    ]