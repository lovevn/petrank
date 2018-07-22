# Generated by Django 2.0.1 on 2018-07-22 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20180722_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('elo_rating', models.IntegerField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.Pet')),
            ],
            options={
                'db_table': 'pet_snapshots',
            },
        ),
    ]