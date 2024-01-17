from django.contrib import admin

from Profile.models import User, Publication


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["nickname", "name", "photo"]


@admin.register(Publication)
class UserAdmin(admin.ModelAdmin):
    list_display = ["image_of_publication", "text_of_publication"]



