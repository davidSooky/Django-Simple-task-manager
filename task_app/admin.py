from django.contrib import admin
from .models import Task, Engineer, Holiday, Comment, Following, Follower
# Register your models here.

admin.site.register(Task)
admin.site.register(Engineer)
admin.site.register(Holiday)
admin.site.register(Comment)
admin.site.register(Following)
admin.site.register(Follower)