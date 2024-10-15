# Generated by Django 5.0.7 on 2024-09-02 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('proid', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('prodescription', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('suppid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('suppname', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocer.product')),
                ('suppid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocer.supplier')),
            ],
        ),
    ]
