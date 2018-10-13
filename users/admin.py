from django.contrib import admin
from .models import Profile,Video,Audio
# Register your models here.

admin.site.register(Profile)
#admin.site.register(Song)
admin.site.register(Video)
admin.site.register(Audio)
