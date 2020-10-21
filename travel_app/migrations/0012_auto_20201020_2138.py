# Generated by Django 3.1.2 on 2020-10-20 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel_app', '0011_city_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travel_journal',
            name='travelers_in_journal',
        ),
        migrations.AddField(
            model_name='travel_journal',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
