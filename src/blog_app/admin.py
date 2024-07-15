from django.contrib import admin

from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    

admin.site.register(Posts, PostsAdmin)