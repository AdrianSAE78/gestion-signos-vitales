# Generated by Django 4.2 on 2024-10-03 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vital_signs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='document_id',
            field=models.IntegerField(unique=True),
        ),
    ]
