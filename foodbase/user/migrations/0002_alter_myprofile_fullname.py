# Generated by Django 4.1.7 on 2023-02-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='fullname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
