# Generated by Django 3.0.7 on 2022-02-13 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20220213_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='questaoresposta',
            name='descricao',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]