# Generated by Django 3.0.6 on 2020-05-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.PositiveIntegerField(default=None, null=True, verbose_name=10),
        ),
    ]
