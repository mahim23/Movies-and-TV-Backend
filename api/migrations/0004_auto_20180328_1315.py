# Generated by Django 2.0.3 on 2018-03-28 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180328_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.CharField(max_length=1000000000, null=True),
        ),
    ]