# Generated by Django 3.2.3 on 2021-07-07 03:20

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_alter_issue_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=markdownx.models.MarkdownxField(default='No description.'),
        ),
    ]
