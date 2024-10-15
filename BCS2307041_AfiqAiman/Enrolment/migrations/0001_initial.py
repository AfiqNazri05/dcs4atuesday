# Generated by Django 5.0.7 on 2024-09-06 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('Activity_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Activity_name', models.CharField(max_length=100)),
                ('Day', models.CharField(max_length=100)),
                ('Time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_ID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Course', models.CharField(max_length=3)),
                ('Phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('Enrollment_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Enrollment_Date', models.DateField()),
                ('Activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enrolment.activities')),
                ('Student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enrolment.student')),
            ],
        ),
    ]
