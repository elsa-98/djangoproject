# Generated by Django 3.0 on 2020-01-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regapp', '0002_leave_s'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_s',
            name='Status',
            field=models.CharField(blank='True', max_length=20, null='True'),
        ),
    ]