from django.contrib import admin
from account.models import Account, ResidentChecklist
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

def getFieldsModel(model):
    return [field.name for field in model._meta.get_fields()]

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'first_name', 'last_name', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class ResidentChecklistAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(ResidentChecklist)


admin.site.register(Account, AccountAdmin)
admin.site.register(ResidentChecklist, ResidentChecklistAdmin)