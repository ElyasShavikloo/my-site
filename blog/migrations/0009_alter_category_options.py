# Generated by Django 4.2.6 on 2023-11-21 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_article_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
    ]