# Generated by Django 3.0.7 on 2022-02-13 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_owasp'),
    ]

    operations = [
        migrations.AddField(
            model_name='questaoresposta',
            name='owasp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.OWASP'),
            preserve_default=False,
        ),
    ]
