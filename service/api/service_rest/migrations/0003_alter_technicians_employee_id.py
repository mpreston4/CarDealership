# Generated by Django 4.0.3 on 2023-04-24 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0002_alter_technicians_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicians',
            name='employee_id',
            field=models.CharField(max_length=200),
        ),
    ]