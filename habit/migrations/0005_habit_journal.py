# Generated by Django 4.0.4 on 2022-05-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0004_habit_planstart'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='journal',
            field=models.TextField(blank=True, null=True),
        ),
    ]
