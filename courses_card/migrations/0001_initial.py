# Generated by Django 4.0.5 on 2022-06-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_duration', models.CharField(max_length=50)),
                ('course_rating', models.IntegerField()),
                ('course_student', models.IntegerField()),
            ],
        ),
    ]
