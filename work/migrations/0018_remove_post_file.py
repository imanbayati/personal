# Generated by Django 3.2.14 on 2022-07-27 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0017_alter_post_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
    ]
