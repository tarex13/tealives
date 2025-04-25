from django.contrib import admin
from tealives.models import Post, Story, Follower_followed, Comments, Activity, Comment_reply, Verify, Logged_in, Security, Files, Chat_member, Chat_room, Chat_text, Chat_log, Post_likes, Media
# Register your models here.

'''class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['auth_username','username','email']}),
        ('Information', {'fields': ['first_name','last_name', 'dob', 'gender','url','p_no','country', 'bio', 'picture', 'user_agent']}),
        ('', {'fields': ['is_active', 'is_disabled', 'is_logged_in']}),
        ('Dates', {'fields': ['date_joined', 'last_login']}),
    ]

    list_display = ('username','email','is_verified','is_disabled','followers','is_logged_in')
    list_filter = ['date_joined']'''
class PostAdmin(admin.ModelAdmin):
    pass
class MediaAdmin(admin.ModelAdmin):
    pass
class StoryAdmin(admin.ModelAdmin):
    pass
class Follower_followedAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed', 'status')
    pass
class CommentsAdmin(admin.ModelAdmin):
    pass
class ActivityAdmin(admin.ModelAdmin):
    pass
class Comment_replyAdmin(admin.ModelAdmin):
    pass
class ActivityAdmin(admin.ModelAdmin):
    pass
class VerifyAdmin(admin.ModelAdmin):
    pass
class Logged_inAdmin(admin.ModelAdmin):
    pass
class SecurityAdmin(admin.ModelAdmin):
    pass
class FilesAdmin(admin.ModelAdmin):
    pass
class ChatMemberAdmin(admin.ModelAdmin):
    pass
class ChatRoomAdmin(admin.ModelAdmin):
    pass
class ChatLogAdmin(admin.ModelAdmin):
    pass
class ChatTextAdmin(admin.ModelAdmin):
    pass 
class PostLikeAdmin(admin.ModelAdmin):
    pass

#admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Post_likes, PostLikeAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Follower_followed, Follower_followedAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Comment_reply, Comment_replyAdmin)
admin.site.register(Verify, VerifyAdmin)
admin.site.register(Logged_in, Logged_inAdmin)
admin.site.register(Files, FilesAdmin)
admin.site.register(Chat_room, ChatRoomAdmin)
admin.site.register(Chat_member, ChatMemberAdmin)
admin.site.register(Chat_log, ChatLogAdmin)
admin.site.register(Chat_text, ChatTextAdmin)