# Generated by Django 4.1 on 2022-08-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_id_alter_l_day_count_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='0', max_length=11, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='l_day_count',
            name='id',
            field=models.CharField(default='0', max_length=11, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='leaveform',
            name='id',
            field=models.CharField(default='0', max_length=11, primary_key=True, serialize=False, unique=True),
        ),
    ]