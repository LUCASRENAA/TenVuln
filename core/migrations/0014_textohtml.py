# Generated by Django 3.0.7 on 2022-02-14 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_questaoresposta_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextoHtml',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=50)),
                ('tipo', models.IntegerField(default=0)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.QuestaoResposta')),
            ],
        ),
    ]
