# Generated by Django 5.1.2 on 2024-11-26 06:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportComApp', '0016_alter_logintable_user_type_festivalratingtable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('USER', 'user'), ('RESTOURANT', 'restaurant'), ('ADMIN', 'admin'), ('RESORT', 'resort'), ('TOURIST', 'tourist')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='AmalgamationGalleryTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(blank=True, null=True, upload_to='')),
                ('AMALGAMATION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportComApp.amalgamationtable')),
            ],
        ),
        migrations.CreateModel(
            name='FestivalGalleryTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(blank=True, null=True, upload_to='')),
                ('FESTIVAL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportComApp.festivaltable')),
            ],
        ),
        migrations.CreateModel(
            name='ViewPointGalleryTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(blank=True, null=True, upload_to='')),
                ('POINT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportComApp.viewpointtable')),
            ],
        ),
    ]