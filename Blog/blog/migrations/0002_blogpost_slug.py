# Generated by Django 4.2.5 on 2023-09-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='hello-world'),
            preserve_default=False,
        ),
    ]
