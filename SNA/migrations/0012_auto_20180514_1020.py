# Generated by Django 2.1.dev20180407215333 on 2018-05-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SNA', '0011_auto_20180513_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SNA.Post'),
        ),
    ]
