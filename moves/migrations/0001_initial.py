# Generated by Django 2.0.3 on 2018-04-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('element', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('power', models.CharField(max_length=50)),
                ('accuracy', models.CharField(max_length=50)),
                ('pp', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('zmove', models.CharField(max_length=200)),
                ('tm', models.BooleanField(default=False)),
            ],
        ),
    ]
