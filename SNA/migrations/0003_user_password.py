# Generated by Django 2.1.dev20180407215333 on 2018-05-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SNA', '0002_auto_20180504_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
    ]