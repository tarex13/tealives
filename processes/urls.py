from django.urls import path
from . import views

urlpatterns = [
    path("v1/user/feed/posts/", views.post_index, name="post_index"),
    path("v1/user/chat/event/<uuid:pk>/", views.chat_log, name="chat_log"),
    path("v1/user/chat/contacts/get/", views.get_chatrooms, name="chat_rooms"),
    #path("v1/user/chat/", views.chat, name="chat"),
    path("v1/user/chat/pc/<str:chat_room>/", views.chat_pc, name="chat_pc"),
    path("v1/user/chat/profile/<str:username>/", views.chat_profile, name="chat_profile"),
    path("v1/user/post/comment/<uuid:p_id>/", views.post_comment, name="post_comment"),
    path("v1/user/details/followers/<str:pk>", views.user_details, name="user_details"),
    path("v1/user/details/bio/<str:pk>", views.user_details, name="user_details"),
    path("v1/user/details/following/<str:pk>", views.user_details, name="user_details"),
    path("v1/user/details/profile/", views.user_details, name="user_details"),
    path("v1/user/search/", views.user_search, name="user_search"),
    path("v1/user/story/<str:user_id>/<str:ref>/<str:story_owner>/", views.story_get, name="story_get"),
    path("v1/user/following/story/", views.following_stories, name="story_get"),
    path("v1/user/relation/follow_unfollow/", views.user_relations, name="user_relations"),
    path("v1/user/post/like/<str:post_id>/", views.post_like, name="post_like")
#     path("", views., name=""),
#     path("", views., name=""),
 ]
