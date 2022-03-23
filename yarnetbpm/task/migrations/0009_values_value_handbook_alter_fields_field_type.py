# Generated by Django 4.0.3 on 2022-03-22 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0002_alter_handbookvalues_field'),
        ('task', '0008_alter_history_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='values',
            name='value_handbook',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='handbook.handbook'),
        ),
        migrations.AlterField(
            model_name='fields',
            name='field_type',
            field=models.CharField(choices=[('STR', 'СТРОКА'), ('INT', 'ЦЕЛОЕ ЧИСЛО'), ('FLT', 'ДРОБНОЕ ЧИСЛО'), ('DAT', 'ДАТА'), ('FIL', 'ФАЙЛ'), ('LIS', 'СПИСОК'), ('USR', 'СОТРУДНИК'), ('CMP', 'ОРГАНИЗАЦИЯ'), ('DIS', 'РАЙОН'), ('NUM', 'НОМЕР'), ('HB', 'СПРАВОЧНИК')], max_length=3),
        ),
    ]
