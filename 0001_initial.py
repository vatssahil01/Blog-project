# Generated by Django 5.1.4 on 2025-01-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogname', models.CharField(max_length=50)),
                ('description', models.EmailField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
