# Generated by Django 4.0.4 on 2022-05-18 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_habit_daterecord'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='daterecord',
            constraint=models.UniqueConstraint(fields=('habit', 'date'), name='unique_date'),
        ),
    ]
