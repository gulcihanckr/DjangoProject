# Generated by Django 2.0.13 on 2019-05-15 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20190515_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News'),
        ),
    ]
