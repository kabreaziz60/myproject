# Generated by Django 4.1.2 on 2022-12-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Birthday', models.DateField(auto_now=True)),
                ('Gender', models.BooleanField(default=True)),
                ('Email', models.EmailField(max_length=50)),
                ('Telephone', models.CharField(max_length=100)),
                ('Pays', models.IntegerField()),
            ],
        ),
    ]