# Generated by Django 3.2.14 on 2022-07-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0011_remove_work_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='category',
        ),
        migrations.AddField(
            model_name='work',
            name='category',
            field=models.ManyToManyField(null=True, to='work.Category'),
        ),
    ]