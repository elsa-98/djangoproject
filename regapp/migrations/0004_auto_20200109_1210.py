# Generated by Django 3.0 on 2020-01-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regapp', '0003_auto_20200109_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_s',
            name='Status',
            field=models.CharField(default='', max_length=20),
        ),
    ]
