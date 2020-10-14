# Generated by Django 3.1.2 on 2020-10-13 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, verbose_name='City to visit')),
                ('tourist_info_adress', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Tourist info details')),
                ('places_worth_visiting', models.TextField(blank=True, default=None, null=True, verbose_name='Places to visit')),
                ('restaurants', models.TextField(blank=True, default=None, null=True, verbose_name='Restaurants')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_title', models.CharField(max_length=25)),
                ('task', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
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
                ('travelers_in_journal', models.ManyToManyField(blank=True, related_name='Travelers_in_journal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_title', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('mean_of_transport', models.CharField(choices=[('plane', 'plane'), ('railway', 'railway'), ('car', 'car'), ('bus', 'bus'), ('other', 'other')], default='other', max_length=20)),
                ('comments', models.TextField(blank=True, null=True)),
                ('budget', models.IntegerField(blank=True, null=True)),
                ('travelers', models.ManyToManyField(blank=True, related_name='Travelers', to=settings.AUTH_USER_MODEL)),
                ('trip_plan', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel_app.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50, verbose_name='Title')),
                ('date_of_creation', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('post_image', models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Pictures')),
                ('blog', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Blog', to='travel_app.blog')),
            ],
        ),
    ]
