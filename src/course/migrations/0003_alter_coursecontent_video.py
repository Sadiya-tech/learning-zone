# Generated by Django 3.2.8 on 2021-11-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_coursecontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]