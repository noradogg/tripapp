from django.db import models
import datetime

# Register your models here
class Member(models.Model):
    name = models.CharField('Name', max_length=255, default="")
    username = models.CharField('@Username', max_length=32, default="")
    email = models.EmailField()
    password = models.CharField('Password', max_length=255, default="")
    profile_img = models.ImageField('Profile Image', upload_to='profile_img/', default="")
    header_img = models.ImageField('Header Image', upload_to='header_img/', default="")
    created_time = models.DateTimeField('Created Time', default="1970-01-01 00:00:00.000000+00:00")
    updated_time = models.DateTimeField('Updated Time', default="1970-01-01 00:00:00.000000+00:00")
    def __str__(self):
        return self.username

class Trip(models.Model):
    date = models.DateField('Trip date', auto_now=False, auto_now_add=False)
    user_id = models.IntegerField('user_id', default="")
    title = models.CharField('Title', max_length=255, default="")
    note = models.TextField('Note', default="")
    created_time = models.DateTimeField('Created Time', default="1970-01-01 00:00:00.000000+00:00")
    updated_time = models.DateTimeField('Updated Time', default="1970-01-01 00:00:00.000000+00:00")

    def __str__(self):
        return f'User #{self.user_id} posted Trip "{self.title}"'

class Action(models.Model):
    trip_id = models.IntegerField('trip_id', default="")
    date = models.DateTimeField('Action Time', auto_now=False, auto_now_add=False, default="1970-01-01 00:00:00.000000+00:00")
    place = models.CharField('Place', max_length=255, default="")
    address = models.CharField('Address', max_length=255, default="")
    note = models.TextField('Note', default="")
    action_img = models.ImageField('Action Image', upload_to='action_img/', default="")
    created_time = models.DateTimeField('Created Time', default="1970-01-01 00:00:00.000000+00:00")
    updated_time = models.DateTimeField('Updated Time', default="1970-01-01 00:00:00.000000+00:00")

    def __str__(self):
        return f'{self.place} is added on Trip #{self.trip_id}'

class Comment(models.Model):
    trip_id = models.IntegerField('trip_id', default="")
    user_id = models.IntegerField('user_id', default="")
    comment = models.TextField('Comment', default="")
    created_time = models.DateTimeField('Created Time', default="1970-01-01 00:00:00.000000+00:00")
    updated_time = models.DateTimeField('Updated Time', default="1970-01-01 00:00:00.000000+00:00")

    def __str__(self):
        return f'User #{self.user_id} comments "{self.comment}" about Trip #{self.trip_id}'

class Favorite(models.Model):
    user_id = models.IntegerField('user_id', default="")
    trip_id = models.IntegerField('trip_id', default="")
    created_time = models.DateTimeField('Created Time', default="1970-01-01 00:00:00.000000+00:00")
    updated_time = models.DateTimeField('Updated Time', default="1970-01-01 00:00:00.000000+00:00")

    def __str__(self):
        return f"User #{self.user_id} add Trip #{self.trip_id} to favorites"

class Following(models.Model):
    user_id = models.IntegerField('user_id', default="")
    following_id = models.IntegerField('following_id', default="")
    created_time = models.DateTimeField('Created Time', default="1970-01-01 00:00:00.000000+00:00")
    updated_time = models.DateTimeField('Updated Time', default="1970-01-01 00:00:00.000000+00:00")

    def __str__(self):
        return f"User #{self.user_id} follows User #{self.following_id}"