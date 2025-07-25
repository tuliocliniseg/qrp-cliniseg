# Generated by Django 5.2.4 on 2025-07-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0005_alter_fator_options_alter_fator_ordem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pergunta',
            options={'ordering': ['numero']},
        ),
        migrations.AddField(
            model_name='pergunta',
            name='numero',
            field=models.PositiveIntegerField(default=9999, help_text='Número sequencial da pergunta para ordenar e controlar a sequência', unique=True),
            preserve_default=False,
        ),
    ]
