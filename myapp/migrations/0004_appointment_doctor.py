# Generated by Django 5.1.3 on 2024-11-13 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
