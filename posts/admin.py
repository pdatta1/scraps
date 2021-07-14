from django.contrib import admin
from .models import Post, ScrapUser


class PostAdmin(admin.ModelAdmin):
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(ScrapUser)
