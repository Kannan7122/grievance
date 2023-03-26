# Generated by Django 4.1.5 on 2023-03-25 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_box'),
    ]

    operations = [
        migrations.CreateModel(
            name='box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]