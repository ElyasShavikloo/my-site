# Generated by Django 4.2.6 on 2023-11-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_projectcategories_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='customer',
            field=models.CharField(max_length=52),
        ),
    ]
