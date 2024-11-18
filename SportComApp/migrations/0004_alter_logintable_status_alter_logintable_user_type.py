# Generated by Django 5.1.2 on 2024-11-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportComApp', '0003_alter_logintable_user_type_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintable',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('USER', 'user'), ('RESORT', 'resort'), ('ADMIN', 'admin'), ('TOURIST', 'tourist'), ('RESTOURANT', 'restaurant')], max_length=20, null=True),
        ),
    ]
