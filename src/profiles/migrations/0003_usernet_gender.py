# Generated by Django 3.1.3 on 2020-11-18 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201118_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernet',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male')], default='male', max_length=8),
        ),
    ]
