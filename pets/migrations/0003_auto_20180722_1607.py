# Generated by Django 2.0.1 on 2018-07-22 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_pet_verified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['verified']},
        ),
        migrations.AddField(
            model_name='petsnapshot',
            name='lost_against',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='petsnapshot_lost_against', to='pets.Pet'),
        ),
        migrations.AddField(
            model_name='petsnapshot',
            name='won_against',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='petsnapshot_won_against', to='pets.Pet'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog')], default='Cat', max_length=16),
        ),
    ]
