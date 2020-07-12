from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm


CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = (
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
        "date_joined",
    )


admin.site.register(CustomUser, CustomUserAdmin)
