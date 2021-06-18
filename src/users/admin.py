from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterForm, UserChangeForm
from .models import CustomUser, Profile


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
