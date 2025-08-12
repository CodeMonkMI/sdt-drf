from django.contrib import admin
from user.models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "membership_date",
    ]

    fieldsets = (
        (
            None,
            {
                "fields": ("username", "password"),
            },
        ),
        (
            "Personal Info:",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "membership_date",
                )
            },
        ),
        (
            "Permissions:",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important Dates:",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
