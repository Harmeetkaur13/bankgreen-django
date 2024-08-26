# Generated by Django 4.1.7 on 2024-08-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0044_alter_brand_options_alter_commentary_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='feature_json',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commentary',
            name='feature_refresh_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
