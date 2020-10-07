from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Profile, Offers
# Register your models here.

class CustomUserAdmin(UserAdmin):
    """ User model admin. """
    list_display = ('email','username','first_name','is_staff','is_commerce')
    list_filter = ('is_commerce', 'is_staff','created','modified')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile model admin ."""
    list_display = ('user','created')
    search_fields = ('user_username','user__email','user__first_name','user__last_name')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Offers)
