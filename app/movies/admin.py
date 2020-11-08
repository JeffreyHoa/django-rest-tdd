from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Movie, CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "title", "genre", "year", "created_date", "updated_date",
    )
    list_display = (
        "title", "genre", "year", "created_date", "updated_date",
    )
    readonly_fields = (
        "created_date", "updated_date",
    )