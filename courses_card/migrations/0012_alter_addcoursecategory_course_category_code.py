# Generated by Django 4.0.5 on 2022-06-14 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_card', '0011_alter_addcoursecategory_course_category_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcoursecategory',
            name='course_category_code',
            field=models.CharField(default=359795, max_length=50),
        ),
    ]
