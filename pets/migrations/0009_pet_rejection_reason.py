# Generated by Django 2.0.4 on 2018-09-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0008_auto_20180902_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='rejection_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]