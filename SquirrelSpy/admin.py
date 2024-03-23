from django.contrib import admin
from .models import User, Squirrel, Sighting

# Register your models here.
admin.site.register(User)
admin.site.register(Squirrel)
admin.site.register(Sighting)