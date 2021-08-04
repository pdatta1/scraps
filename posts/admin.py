from django.contrib import admin
from .models import Post, ScrapUser, Profile, Comment , SubComment


class PostAdmin(admin.ModelAdmin):
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Post


class CommentAdmin(admin.ModelAdmin):
    list_dispay = ('profile', 'post', 'context', 'date_created')
    list_filter = ('active', 'date_created')
    search_fields = [
        'profile', 'context'
    ]
    actions = 'approve_comments'

    def approve_comments(self, request, queryset):
        return queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(SubComment)
admin.site.register(ScrapUser)
admin.site.register(Profile)
