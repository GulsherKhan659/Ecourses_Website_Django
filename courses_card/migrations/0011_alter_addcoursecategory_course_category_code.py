# Generated by Django 4.0.5 on 2022-06-14 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_card', '0010_alter_addcoursecategory_course_category_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcoursecategory',
            name='course_category_code',
            field=models.CharField(default=539790, max_length=50),
        ),
    ]