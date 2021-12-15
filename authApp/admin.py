from django.contrib import admin

# Register your models here.

from .models.user import User

# Register your models here.
admin.site.register(User)
