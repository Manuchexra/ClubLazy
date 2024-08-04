# Generated by Django 5.0.6 on 2024-06-01 07:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_str', models.TextField(blank=True)),
                ('question_img', models.ImageField(blank=True, upload_to='')),
                ('question_type1', models.CharField(choices=[('Katta sinflar', 'Katta sinflar'), ('Kichik sinflar', 'Kichik sinflar')], max_length=100)),
                ('question_subject', models.CharField(choices=[('Dasturlash', 'Dasturlash'), ('Matematika', 'Matematika'), ('Fizika', 'Fizika')], max_length=15)),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_student', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
