# Generated by Django 3.1.3 on 2020-11-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_usernet_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernet',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=8),
        ),
        migrations.AlterField(
            model_name='usernet',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]