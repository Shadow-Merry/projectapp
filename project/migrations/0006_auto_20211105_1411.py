# Generated by Django 3.2.8 on 2021-11-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20211105_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]