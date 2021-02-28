from django.contrib import admin
from .models import User, ReaderProfile, AdminProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','password','first_name','last_name',
                    'email','is_active','is_superuser','is_reader','is_admin',
                    'last_login','date_joined')

@admin.register(ReaderProfile)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'user_id')

@admin.register(AdminProfile)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'user_id')