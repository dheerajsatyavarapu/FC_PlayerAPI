# Generated by Django 4.0.2 on 2022-02-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='overall',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='p_id',
            field=models.IntegerField(),
        ),
    ]
