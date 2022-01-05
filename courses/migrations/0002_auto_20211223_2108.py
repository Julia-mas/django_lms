# Generated by Django 3.2.9 on 2021-12-23 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_rename_groups_nationality_groups_groups_country'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_group', to='groups.groups'),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(max_length=100),
        ),
    ]