# Generated by Django 5.0.7 on 2024-09-03 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('membershipid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('membershipname', models.CharField(max_length=100)),
                ('emailaddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieid', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('movietitle', models.CharField(max_length=100)),
                ('movieduration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('rentalcode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('startdate', models.DateField()),
                ('returndate', models.DateField()),
                ('membershipid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.membership')),
                ('movieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.movie')),
            ],
        ),
    ]
