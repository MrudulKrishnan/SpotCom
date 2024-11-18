# Generated by Django 5.1.2 on 2024-11-07 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportComApp', '0004_alter_logintable_status_alter_logintable_user_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TuristTable',
            new_name='TouristTable',
        ),
        migrations.RenameField(
            model_name='amalgamationtable',
            old_name='TURIST',
            new_name='TOURIST',
        ),
        migrations.RenameField(
            model_name='festiveltable',
            old_name='TURIST',
            new_name='TOURIST',
        ),
        migrations.RenameField(
            model_name='parkingsopttable',
            old_name='TURIST',
            new_name='TOURIST',
        ),
        migrations.RenameField(
            model_name='viewpointtable',
            old_name='TURIST',
            new_name='TOURIST',
        ),
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('TOURIST', 'tourist'), ('RESTOURANT', 'restaurant'), ('USER', 'user'), ('RESORT', 'resort'), ('ADMIN', 'admin')], max_length=20, null=True),
        ),
    ]