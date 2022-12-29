from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account,Playlist,Review


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    # def get_fields(self, request, obj):
    #     if request.user.is_superuser:
    #         return ('id','email', 'username','password', 'date_joined',
    #                 'last_login', 'is_admin','is_active', 'is_staff','is_superuser')
        
        


admin.site.register(Account, AccountAdmin)
admin.site.register(Playlist)
admin.site.register(Review)
