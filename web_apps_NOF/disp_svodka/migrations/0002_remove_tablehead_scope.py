# Generated by Django 3.2.9 on 2021-12-06 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disp_svodka', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablehead',
            name='scope',
        ),
    ]
