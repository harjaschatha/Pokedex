# Generated by Django 2.0.3 on 2018-03-31 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0004_move'),
    ]

    operations = [
        migrations.RenameField(
            model_name='move',
            old_name='acc',
            new_name='accuracy',
        ),
        migrations.RenameField(
            model_name='move',
            old_name='cat',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='move',
            old_name='type',
            new_name='element',
        ),
        migrations.RenameField(
            model_name='move',
            old_name='pow',
            new_name='power',
        ),
        migrations.RemoveField(
            model_name='move',
            name='eff',
        ),
        migrations.AddField(
            model_name='move',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='move',
            name='zmove',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
