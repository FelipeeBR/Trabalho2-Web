# Generated by Django 4.1 on 2022-08-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabDois', '0003_aluno_delete_cliente_delete_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='periodo_ingresso',
            field=models.CharField(max_length=50, verbose_name='Periodo'),
        ),
    ]
