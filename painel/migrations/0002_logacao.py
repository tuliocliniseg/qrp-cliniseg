# Generated by Django 5.2.4 on 2025-07-15 21:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LogAcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.CharField(choices=[('criar', 'Criar'), ('editar', 'Editar'), ('excluir', 'Excluir'), ('login', 'Login'), ('logout', 'Logout')], max_length=20)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('executado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='acoes_executadas_painel', to=settings.AUTH_USER_MODEL)),
                ('usuario_alvo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='acoes_recebidas_painel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
