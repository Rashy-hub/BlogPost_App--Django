# Generated by Django 5.1.4 on 2024-12-29 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
    ]
