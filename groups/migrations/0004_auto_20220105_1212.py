# Generated by Django 3.2.9 on 2022-01-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_remove_teachers_group'),
        ('groups', '0003_rename_groups_nationality_groups_groups_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='teachers',
            field=models.ManyToManyField(related_name='groups', to='teachers.Teachers'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='members_qty',
            field=models.IntegerField(default=5),
        ),
    ]