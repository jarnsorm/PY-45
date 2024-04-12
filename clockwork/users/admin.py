from django.contrib import admin

from users.models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'lastname', 'firstname', 'date_of_registration']


admin.site.register(Users, UsersAdmin)