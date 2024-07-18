from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
    # fields = ('',
    #           'name',)
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
        ]

admin.site.register(CustomUser, CustomUserAdmin)