# Generated by Django 4.2.6 on 2023-11-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='projects/images')),
                ('image2', models.ImageField(upload_to='projects/images')),
                ('image3', models.ImageField(upload_to='projects/images')),
                ('image4', models.ImageField(upload_to='projects/images')),
                ('image5', models.ImageField(upload_to='projects/images')),
                ('image6', models.ImageField(upload_to='projects/images')),
                ('image7', models.ImageField(upload_to='projects/images')),
                ('body', models.TextField()),
                ('extra_details', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.CharField(max_length=51)),
                ('about_customer', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('category', models.ManyToManyField(related_name='projects', to='home.projectcategories')),
            ],
        ),
    ]
