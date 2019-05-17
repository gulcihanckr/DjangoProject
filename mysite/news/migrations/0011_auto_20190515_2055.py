# Generated by Django 2.0.13 on 2019-05-15 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20190515_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['published_date']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News'),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('news', 'id')},
        ),
    ]
