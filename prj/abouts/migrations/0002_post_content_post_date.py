# Generated by Django 4.2 on 2023-05-05 18:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('abouts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
