# Generated by Django 2.0 on 2019-02-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20190225_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='dob',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='id_number',
            field=models.IntegerField(null=True),
        ),
    ]
