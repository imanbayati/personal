# Generated by Django 3.2.14 on 2022-07-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0009_delete_quillpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]
