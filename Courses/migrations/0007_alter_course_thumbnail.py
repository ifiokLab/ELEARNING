# Generated by Django 4.0.2 on 2022-02-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0006_alter_course_description_alter_course_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='thumbnail'),
        ),
    ]