# Generated by Django 4.0.4 on 2022-05-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_headliner'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='total_tickets',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]