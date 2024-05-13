from django.contrib import admin
from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'email', 'date_of_registration', 'last_login']


admin.site.register(Account, AccountAdmin)