# Generated by Django 5.1.2 on 2024-11-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportComApp', '0012_resortratingtable_resort_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('TOURIST', 'tourist'), ('ADMIN', 'admin'), ('RESORT', 'resort'), ('USER', 'user'), ('RESTOURANT', 'restaurant')], max_length=20, null=True),
        ),
    ]