# Generated by Django 4.0.4 on 2022-05-19 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0005_habit_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
