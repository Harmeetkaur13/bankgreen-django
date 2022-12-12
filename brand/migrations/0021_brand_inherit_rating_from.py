# Generated by Django 4.0.7 on 2022-12-08 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0020_migrate_cms_field_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='inherit_rating_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='brand.brand'),
        ),
    ]
