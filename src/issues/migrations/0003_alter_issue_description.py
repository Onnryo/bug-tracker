# Generated by Django 3.2.3 on 2021-07-06 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_issue_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(default='No Description.'),
        ),
    ]
