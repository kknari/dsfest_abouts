# Generated by Django 4.2 on 2023-05-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abouts', '0002_post_content_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]