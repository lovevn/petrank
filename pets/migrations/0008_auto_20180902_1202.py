# Generated by Django 2.0.1 on 2018-09-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_auto_20180902_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Other', 'Other')], default='Cat', max_length=16),
        ),
    ]
