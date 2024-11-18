# Generated by Django 5.1.2 on 2024-11-07 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportComApp', '0008_alter_logintable_status_alter_logintable_user_type_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RestaourantTable',
            new_name='RestaurantTable',
        ),
        migrations.AlterField(
            model_name='logintable',
            name='status',
            field=models.CharField(choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('TOURIST', 'tourist'), ('ADMIN', 'admin'), ('RESORT', 'resort'), ('RESTOURANT', 'restaurant'), ('USER', 'user')], max_length=20, null=True),
        ),
    ]
