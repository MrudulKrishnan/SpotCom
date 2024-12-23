# Generated by Django 5.1.2 on 2024-11-07 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportComApp', '0006_rename_parkingsopttable_parkingspottable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoshoottable',
            name='TOURIST',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SportComApp.touristtable'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('RESORT', 'resort'), ('RESTOURANT', 'restaurant'), ('TOURIST', 'tourist'), ('USER', 'user'), ('ADMIN', 'admin')], max_length=20, null=True),
        ),
    ]
