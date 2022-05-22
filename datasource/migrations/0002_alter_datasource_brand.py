# Generated by Django 3.2.12 on 2022-05-22 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
        ('datasource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='datasources', related_query_name='datasource', to='brand.brand'),
        ),
    ]
