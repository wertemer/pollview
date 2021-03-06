# Generated by Django 2.2.10 on 2021-06-22 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('date_begin', models.DateTimeField(auto_now=True)),
                ('date_end', models.DateTimeField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Аноним', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprosnik.Answers')),
                ('f_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprosnik.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(1, 'Текст'), (2, 'Выбор варианта'), (3, 'Множественный выбор')], default=1, max_length=100)),
                ('f_poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprosnik.Poll')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='f_questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oprosnik.Questions'),
        ),
    ]
