# Generated by Django 3.0.10 on 2020-11-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialfeature',
            name='publication_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specialfeature',
            name='publication_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
