# Generated by Django 3.2.5 on 2021-07-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20210726_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('code', 'code'), ('mobile review', 'mobile review'), ('vlog', 'vlog'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('film making', 'film making'), ('cooking', 'cooking')], max_length=255),
        ),
    ]
