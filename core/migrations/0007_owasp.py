# Generated by Django 3.0.7 on 2022-02-13 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220212_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='OWASP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('posicao', models.IntegerField()),
                ('ano', models.IntegerField()),
            ],
        ),
    ]
