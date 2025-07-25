# Generated by Django 5.2.4 on 2025-07-14 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setor', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=20)),
                ('faixa_etaria', models.CharField(max_length=50)),
                ('q1', models.IntegerField()),
                ('q2', models.IntegerField()),
                ('q3', models.IntegerField()),
                ('q4', models.IntegerField()),
                ('q5', models.IntegerField()),
                ('q6', models.IntegerField()),
                ('q7', models.IntegerField()),
                ('q8', models.IntegerField()),
                ('q9', models.IntegerField()),
                ('q10', models.IntegerField()),
                ('q11', models.IntegerField()),
                ('q12', models.IntegerField()),
                ('q13', models.IntegerField()),
                ('q14', models.IntegerField()),
                ('q15', models.IntegerField()),
                ('q16', models.IntegerField()),
                ('q17', models.IntegerField()),
                ('q18', models.IntegerField()),
                ('q19', models.IntegerField()),
                ('q20', models.IntegerField()),
                ('q21', models.IntegerField()),
                ('q22', models.IntegerField()),
                ('q23', models.IntegerField()),
                ('q24', models.IntegerField()),
                ('q25', models.IntegerField()),
                ('q26', models.IntegerField()),
                ('q27', models.IntegerField()),
                ('q28', models.IntegerField()),
                ('q29', models.IntegerField()),
                ('q30', models.IntegerField()),
                ('q31', models.IntegerField()),
                ('q32', models.IntegerField()),
                ('q33', models.IntegerField()),
                ('q34', models.IntegerField()),
                ('q35', models.IntegerField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa')),
            ],
        ),
    ]
