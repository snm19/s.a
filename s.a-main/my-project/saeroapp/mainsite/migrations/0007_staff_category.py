# Generated by Django 3.2.7 on 2022-09-02 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_alter_staff_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='mainsite.category'),
        ),
    ]
