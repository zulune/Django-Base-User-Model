from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
# Register your models here.

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    search_fields = ['email']
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'admin',)
    list_filter = ('admin', 'timestamp', 'last_login', )

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal data', {'fields': ('first_name', 'last_name', )}),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    ordering = ('email', )
    filter_horizontal = ()


# Remove Group Model
admin.site.unregister(Group)


admin.site.register(User, UserAdmin)