
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['f_name', 'l_name', 'u_name', 'e_mail', 'is_staff', 'is_active', 'date_joined', ]

    # fieldsets = UserAdmin.fieldsets + ( # new
    #     (None, {'fields': ('f_name',)}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + ( # new
    #     (None, {'fields': ('l_name',)}),
    # )

admin.site.register(CustomUser, CustomUserAdmin)