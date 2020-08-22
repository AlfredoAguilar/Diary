from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from BaseProject.apps.custom_user.models import User


admin.site.register(User, UserAdmin)
