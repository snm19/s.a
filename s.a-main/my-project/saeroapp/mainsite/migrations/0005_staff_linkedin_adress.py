# Generated by Django 3.2.7 on 2022-08-31 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_staff_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='linkedin_adress',
            field=models.TextField(null=True),
        ),
    ]