# Generated by Django 3.2.7 on 2021-09-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.IntegerField(default='', verbose_name='trip_id')),
                ('date', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Action Time')),
                ('place', models.CharField(default='', max_length=255, verbose_name='Place')),
                ('address', models.CharField(default='', max_length=255, verbose_name='Address')),
                ('note', models.TextField(default='', verbose_name='Note')),
                ('action_img', models.ImageField(default='', upload_to='action_img/', verbose_name='Action Image')),
                ('created_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Updated Time')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.IntegerField(default='', verbose_name='trip_id')),
                ('user_id', models.IntegerField(default='', verbose_name='user_id')),
                ('comment', models.TextField(default='', verbose_name='Comment')),
                ('created_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Updated Time')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default='', verbose_name='user_id')),
                ('trip_id', models.IntegerField(default='', verbose_name='trip_id')),
                ('created_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Updated Time')),
            ],
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default='', verbose_name='user_id')),
                ('following_id', models.IntegerField(default='', verbose_name='following_id')),
                ('created_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Updated Time')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Name')),
                ('username', models.CharField(default='', max_length=32, verbose_name='@Username')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(default='', max_length=255, verbose_name='Password')),
                ('profile_img', models.ImageField(default='', upload_to='profile_img/', verbose_name='Profile Image')),
                ('header_img', models.ImageField(default='', upload_to='header_img/', verbose_name='Header Image')),
                ('created_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Updated Time')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Trip date')),
                ('user_id', models.IntegerField(default='', verbose_name='user_id')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Title')),
                ('note', models.TextField(default='', verbose_name='Note')),
                ('created_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(default='1970-01-01 00:00:00.000000+00:00', verbose_name='Updated Time')),
            ],
        ),
    ]
