# Generated by Django 2.2.10 on 2021-06-22 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oprosnik', '0021_auto_20210622_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opros',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('date_begin', models.DateTimeField(auto_now=True)),
                ('date_end', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='f_opros',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='oprosnik.Opros'),
        ),
    ]