# Generated by Django 3.2.3 on 2021-06-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_agendamento_agendamentomarcado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='agendamentoMarcado',
            field=models.CharField(choices=[(1, 'Confirmado'), (0, 'Aguardando confirmação')], default=False, max_length=1),
        ),
    ]
