from django.contrib import admin
from .models import Blog, BlogType, User


# Register your models here.
# admin.site.register(Article)

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'blog_type', 'get_read_num', 'author', 'created_time', 'last_update_time')
    ordering = ('-id',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    ordering = ('-id',)

