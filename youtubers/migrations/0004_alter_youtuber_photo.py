# Generated by Django 3.2.6 on 2021-08-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0003_alter_youtuber_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='photo',
            field=models.ImageField(upload_to='staticfiles/ytubers/%Y/%m'),
        ),
    ]
