# Generated by Django 3.1.4 on 2020-12-26 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardlist',
            name='board_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 23, 52, 6, 525430)),
        ),
    ]
