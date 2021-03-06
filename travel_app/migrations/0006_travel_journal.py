# Generated by Django 3.1.2 on 2020-10-14 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel_app', '0005_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_title', models.CharField(max_length=50)),
                ('places', models.TextField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('best_moments', models.TextField(blank=True, default=None, null=True)),
                ('best_pictures', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('travel', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel_app.travel')),
                ('travelers_in_journal', models.ManyToManyField(blank=True, related_name='Travelers_in_journal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
