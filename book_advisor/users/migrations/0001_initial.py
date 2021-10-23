# Generated by Django 3.1.4 on 2021-10-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('advisor_name', models.CharField(max_length=100, unique=True)),
                ('advisor_photo', models.FileField(blank=True, null=True, upload_to='users/advisor_pics/')),
                ('advisor_photo_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]