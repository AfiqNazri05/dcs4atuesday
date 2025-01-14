# Generated by Django 5.0.7 on 2024-10-01 02:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentage',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='student',
            name='studentemail',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mentorid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.mentor'),
        ),
    ]
