# Generated by Django 4.2.1 on 2023-10-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_work_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_exp',
            name='currently_working',
            field=models.BooleanField(default=1),
        ),
    ]
