# Generated by Django 2.0.13 on 2019-05-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190412_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
