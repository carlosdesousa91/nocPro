# Generated by Django 3.1.7 on 2021-03-11 01:28

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acionamentos', '0008_acionamento_ativos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acionamento',
            name='ativos',
            field=models.CharField(choices=[('weqeq', 'weqeq'), ('CENTRAL_1_1_1', 'CENTRAL_1_1_1'), ('CENTRAL_1_1', 'CENTRAL_1_1'), ('TESTE-SONORO-POPUP-VIEW', 'TESTE-SONORO-POPUP-VIEW'), ('DAGSER-PE-EDUDRIVE-STORAGE-REC02_1', 'DAGSER-PE-EDUDRIVE-STORAGE-REC02_1'), ('DAGSER-PE-EDUDRIVE-STORAGE-REC01_1', 'DAGSER-PE-EDUDRIVE-STORAGE-REC01_1'), ('DAGSER-PE-EDUDRIVE-PROXY-REC02_1', 'DAGSER-PE-EDUDRIVE-PROXY-REC02_1'), ('DAGSER-PE-EDUDRIVE-PROXY-REC01_1', 'DAGSER-PE-EDUDRIVE-PROXY-REC01_1'), ('DAGSER-PE-EDUDRIVE-MON-REC01_1_1', 'DAGSER-PE-EDUDRIVE-MON-REC01_1_1'), ('POLLER-DISPLAY_1_3', 'POLLER-DISPLAY_1_3'), ('POLLER-DISPLAY_1_2', 'POLLER-DISPLAY_1_2'), ('POLLER-DISPLAY_1_1', 'POLLER-DISPLAY_1_1'), ('POLLER-DISPLAY_1', 'POLLER-DISPLAY_1'), ('REMOTE-SERVER-TESTE', 'REMOTE-SERVER-TESTE'), ('CENTRAL_1', 'CENTRAL_1'), ('TESTE-NOVO-IC-ADICIONADO', 'TESTE-NOVO-IC-ADICIONADO'), ('teste-RELOAD-remote-server-_NOVO-IC', 'teste-RELOAD-remote-server-_NOVO-IC'), ('TESTE-BUG-HOST-REMOTE-SERVER', 'TESTE-BUG-HOST-REMOTE-SERVER'), ('Remote-Server-Hml', 'Remote-Server-Hml'), ('PoP-PE-CLIENTE-UNIVASF-Petrolina_REPEPE', 'PoP-PE-CLIENTE-UNIVASF-Petrolina_REPEPE'), ('PoP-PE-CLIENTE-UFPE-Caruaru_REPEPE', 'PoP-PE-CLIENTE-UFPE-Caruaru_REPEPE'), ('PoP-PE-CLIENTE-SECTI-Armazem-Caruaru_REPEPE', 'PoP-PE-CLIENTE-SECTI-Armazem-Caruaru_REPEPE'), ('PoP-PE-CLIENTE-POA-Salgueiro_REPEPE', 'PoP-PE-CLIENTE-POA-Salgueiro_REPEPE'), ('PoP-PE-CLIENTE-POA-Garanhuns_REPEPE', 'PoP-PE-CLIENTE-POA-Garanhuns_REPEPE'), ('PoP-PE-CLIENTE-POA-Caruaru_REPEPE', 'PoP-PE-CLIENTE-POA-Caruaru_REPEPE'), ('PoP-PE-CLIENTE-POA-BeloJardim_REPEPE', 'PoP-PE-CLIENTE-POA-BeloJardim_REPEPE'), ('PoP-PE-CLIENTE-ITEP-Caruaru_REPEPE', 'PoP-PE-CLIENTE-ITEP-Caruaru_REPEPE'), ('PoP-PE-CLIENTE-ITEP-Garanhuns_REPEPE', 'PoP-PE-CLIENTE-ITEP-Garanhuns_REPEPE'), ('PoP-PE-CLIENTE-IFPE-Garanhuns_REPEPE', 'PoP-PE-CLIENTE-IFPE-Garanhuns_REPEPE'), ('PoP-PE-CLIENTE-IFPE-BeloJardim_REPEPE', 'PoP-PE-CLIENTE-IFPE-BeloJardim_REPEPE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='acionamento',
            name='nome',
            field=models.CharField(max_length=100, verbose_name=django.contrib.auth.models.User),
        ),
    ]