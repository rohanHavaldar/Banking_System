from django.contrib import admin

admin.site.site_header="Central Bank"

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_id', 'contact', 'balance']
    search_fields =['username']

class DepositAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_id', 'contact', 'amount']
    search_fields =['username']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_id', 'contact', 'amount', 'action', 'status']
    search_fields =['username']

# Register your models here.
from .models import User
from .models import Action
from .models import History

admin.site.register(User, UserAdmin)
admin.site.register(Action, DepositAdmin)
admin.site.register(History, HistoryAdmin)
