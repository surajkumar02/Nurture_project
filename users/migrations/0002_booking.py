# Generated by Django 3.1.4 on 2021-10-23 05:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.advisor')),
            ],
        ),
    ]
