# Generated by Django 3.0.7 on 2022-02-13 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_owasp_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owasp',
            name='descricao',
            field=models.TextField(max_length=1000),
        ),
    ]
