# Generated by Django 4.2.1 on 2023-06-03 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_change',
            field=models.DateTimeField(),
        ),
    ]
