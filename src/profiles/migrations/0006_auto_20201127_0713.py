# Generated by Django 3.1.3 on 2020-11-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20201119_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernet',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=8),
        ),
    ]
