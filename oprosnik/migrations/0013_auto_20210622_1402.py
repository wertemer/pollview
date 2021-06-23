# Generated by Django 2.2.10 on 2021-06-22 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oprosnik', '0012_auto_20210622_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('desc', models.TextField(default='')),
                ('date_begin', models.DateTimeField(auto_now=True)),
                ('date_end', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='questions',
            name='f_poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprosnik.Polls'),
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
    ]