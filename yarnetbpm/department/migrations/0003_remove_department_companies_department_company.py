# Generated by Django 4.0.2 on 2022-03-06 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('department', '0002_remove_department_organizations_department_companies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='companies',
        ),
        migrations.AddField(
            model_name='department',
            name='company',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.company'),
        ),
    ]
