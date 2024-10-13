# Generated by Django 5.1.1 on 2024-10-12 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0008_alter_participante_antecedentes_enfermedad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hecho',
            name='tipo_violencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.tipoviolencia'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]