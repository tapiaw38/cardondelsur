from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Profile, Offers, City
# Register your models here.

class CustomUserAdmin(UserAdmin):
    """ User model admin. """
    list_display = ('email','username','first_name','is_staff','is_commerce', 'is_verfied')
    list_filter = ('is_commerce', 'is_staff','created','modified')
    
    actions = ['is_commerce','is_not_commerce']

    def is_commerce(self, request, queryset):
        '''Make commerce is true'''
        queryset.update(is_commerce=True)
    is_commerce.short_description = 'Make selected user is true'

    def is_not_commerce(self, request, queryset):
        '''Make commerce is true'''
        queryset.update(is_commerce=False)
    is_not_commerce.short_description = 'Make selected user is false'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile model admin ."""
    list_display = ('user','commerce_name','phone_number','created')
    search_fields = ('user_username','user__email','user__first_name','user__last_name')

class OffersAdmin(admin.ModelAdmin):
    ''' Offers  '''
    pass

admin.site.register(User, CustomUserAdmin)
admin.site.register(Offers)
admin.site.register(City)
