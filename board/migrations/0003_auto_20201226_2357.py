# Generated by Django 3.1.4 on 2020-12-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20201226_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardlist',
            name='board_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
