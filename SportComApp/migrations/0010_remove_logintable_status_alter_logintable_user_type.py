# Generated by Django 5.1.2 on 2024-11-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportComApp', '0009_rename_restaouranttable_restauranttable_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logintable',
            name='status',
        ),
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('RESORT', 'resort'), ('ADMIN', 'admin'), ('USER', 'user'), ('TOURIST', 'tourist'), ('RESTOURANT', 'restaurant')], max_length=20, null=True),
        ),
    ]
