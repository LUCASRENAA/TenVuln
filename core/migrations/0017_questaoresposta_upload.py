# Generated by Django 3.0.7 on 2022-02-18 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20220218_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='questaoresposta',
            name='upload',
            field=models.FileField(default='/', upload_to='vulneraveis/'),
        ),
    ]