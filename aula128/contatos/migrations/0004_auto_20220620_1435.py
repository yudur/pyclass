# Generated by Django 2.2.3 on 2022-06-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_auto_20220619_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]