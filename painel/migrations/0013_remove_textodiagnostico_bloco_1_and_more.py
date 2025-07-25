# Generated by Django 5.2.4 on 2025-07-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0012_textodiagnostico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textodiagnostico',
            name='bloco_1',
        ),
        migrations.RemoveField(
            model_name='textodiagnostico',
            name='bloco_2',
        ),
        migrations.RemoveField(
            model_name='textodiagnostico',
            name='titulo',
        ),
        migrations.AddField(
            model_name='textodiagnostico',
            name='texto_final',
            field=models.TextField(blank=True, default='', verbose_name='Texto Final do Diagnóstico'),
        ),
        migrations.AddField(
            model_name='textodiagnostico',
            name='texto_inicial',
            field=models.TextField(blank=True, default='', verbose_name='Texto Inicial do Diagnóstico'),
        ),
    ]
