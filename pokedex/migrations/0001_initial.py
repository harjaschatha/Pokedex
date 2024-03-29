# Generated by Django 2.0.2 on 2018-03-18 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('dex_num', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.URLField()),
                ('name', models.CharField(max_length=200)),
                ('types', models.CharField(max_length=200)),
                ('species', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
            ],
        ),
    ]
