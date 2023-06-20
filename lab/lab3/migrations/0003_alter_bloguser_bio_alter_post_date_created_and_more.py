# Generated by Django 4.2.1 on 2023-06-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0002_alter_comment_date_created_alter_post_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_change',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
