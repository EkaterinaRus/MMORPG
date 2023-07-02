from django.contrib import admin

from .models import Post, Category, Reply


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category', 'short_name_category')

admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reply)
