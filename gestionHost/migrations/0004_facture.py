# Generated by Django 4.0.5 on 2022-08-24 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionHost', '0003_categorie_menuarticles_alter_chambre_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionHost.client')),
            ],
        ),
    ]
