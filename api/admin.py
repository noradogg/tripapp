from django.contrib import admin
from api.models import Member, Trip, Action, Comment, Favorite, Following

# Register your models here.
admin.site.register(Member)
admin.site.register(Trip)
admin.site.register(Action)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Following)