# Generated by Django 2.2.10 on 2021-06-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oprosnik', '0006_auto_20210622_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='desc',
            field=models.TextField(),
        ),
    ]
