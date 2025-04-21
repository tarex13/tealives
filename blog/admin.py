from django.contrib import admin
from blog.models import Post, Category, Comment, Adminpost, User


class PostAdmin(admin.ModelAdmin):
    list_filter = ['created_on']
    list_display = ('id', 'title', 'created_on', 'was_published_recently')


class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass
class AdminpostAdmin(admin.ModelAdmin):
    pass
class UserAdmin(admin.ModelAdmin):
    list_filter = ['created_on']
    list_display = ('id', 'username', 'dob', 'followers', 'country')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Adminpost, AdminpostAdmin)
admin.site.register(User, UserAdmin)
