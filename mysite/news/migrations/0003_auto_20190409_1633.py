# Generated by Django 2.0.13 on 2019-04-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190404_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]