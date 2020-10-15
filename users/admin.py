'''
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('id', 'first_name', 'last_name', 'username', 'phone', 'email',)
    list_display_links = ('id', 'username')
    #list_editable = ('first_name', 'last_name')

admin.site.register(CustomUser, CustomUserAdmin)
'''


from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserNetAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email', 'first_name', 'last_name',  'phone')}),
    )


admin.site.register(CustomUser, UserNetAdmin)