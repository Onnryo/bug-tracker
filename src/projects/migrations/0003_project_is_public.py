# Generated by Django 3.2.3 on 2021-07-01 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_public',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
