from ast import Not
from itertools import chain
from random import choices
from tabnanny import verbose
from tokenize import Comment
import uuid
from email.policy import default
from enum import unique
from xmlrpc.client import DateTime
from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
import datetime
from datetime import timedelta
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.conf import settings
from cloudinary.models import CloudinaryField
User = settings.AUTH_USER_MODEL


class Files(models.Model):
    f_id = models.CharField(max_length=225)
    file_type_choices = [
        ('U', 'User Picture'),
        ('S', 'Story Picture'),
        ('P', 'Post Picture'),
    ]
    #username = models.CharField()
    name = models.CharField(max_length=225, unique=True) # Should be a set of random characters
    base = models.CharField(
        max_length = 20,
        choices = file_type_choices,
        blank = False,
        )
    
    uploadedFile = models.FileField(verbose_name="file", upload_to='uploads/%Y/%m/%d/')
    file_type = models.CharField(max_length=10, blank=True)
    file_mime = models.CharField(max_length=50, blank=True)
    #date = models.DateTimeField(now)
    #base64 = models.TextField()
    #blob_url = models.CharField(max_length=225)
    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
   class Templates(models.IntegerChoices):
        Template_1 = 1
        Template_2 = 2
        Template_3 = 3
        Template_4 = 4

   p_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
   desc = models.CharField(max_length=255, blank=True)
   # file0 = models.CharField(max_length=255,default="")
   title = models.SlugField(max_length=100, blank=True)
   top_text = models.CharField(max_length=255, blank=True)
   location = models.CharField(max_length=255, blank=True)
   alt_text = models.CharField(max_length=255, blank=True)
   files = models.ManyToManyField(Files)
   link = models.URLField(blank=True)
   template = models.IntegerField(choices=Templates.choices)
   is_disabled = models.BooleanField(
    ('disabled'),
    default=False,
    help_text=_(
     'Designates whether this users post should be disabled. '
      'Select this when post violates community guidelines.'
      ),
      )
   is_deleted = models.BooleanField(
     ('deleted'),
     default=False,
     help_text=_(
      'Designates whether this post is deleted.'
       ),
      )
   tagged = models.ManyToManyField(User, related_name="Username", blank=True)
   last_modified = models.DateTimeField(_('last modified'),auto_now_add=True)
   created_on = models.DateTimeField(auto_now_add=True)
   def likes(self):
       likes = Post_likes.objects.filter(post=self.p_id, status="L")
       return(likes.count())
   def comments(self):
       comments = Comments.objects.filter(c_post = self.p_id)
       return(comments.count())

   def __str__(self):
       return '%s' % (self.p_id)
  
  
def generate_random_filename():
    # Generate a random UUID and append the file extension
    return f"{uuid.uuid4()}"

class photos(models.Model):
    title = models.CharField(_(""), max_length=100, default=generate_random_filename())
    image = CloudinaryField('image')

class Comments(models.Model):
    c_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="+")
    c_sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="+") # The person commenting
    c_receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="+") # The owner of the post being commented
    c_comment_text = models.CharField(max_length=255) # The text of the post
    c_created = models.DateTimeField(auto_now=True)
    c_modified = models.DateTimeField(auto_now_add=True)
    c_is_deleted = models.BooleanField(default=False)
    c_likes = models.IntegerField(default=0)
    def __str__(self):
       return '%s -> %s' % (self.c_post, self.c_sender)

    
class Comment_reply(models.Model):
    c_comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="+",default="")
    r_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+",default="")
    r_receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="+",default="")
    # comment_id = models.ForeignKey(Comments, on_delete=models.CASCADE)
    r_comment_text = models.CharField(max_length=255)
    r_time = models.DateTimeField()
    r_is_deleted = models.BooleanField(default=False)
    r_likes = models.IntegerField()
    r_reply = models.CharField(max_length=255)

class Post_likes(models.Model):
    post = models.ForeignKey(Post, to_field="p_id",on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likeChoices = [
        ('L', 'Liked'),
        ('U', 'Unliked'),
    ]
    status = models.CharField(choices=likeChoices, max_length=15)
    date_liked = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)

class Story(models.Model):
    s_id = models.CharField(max_length=225)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story_id = models.CharField(max_length=255)
    fileName = models.ForeignKey(Files, on_delete=models.CASCADE, blank=True)
    text = models.CharField(max_length=255, blank=True)
class Follower_followed(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed", default="", null=False, blank=False) # The follower is the person performing the action 
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower", default="", null=False, blank=False) # The followed is the person being followed
    statusChoices = [
        ('N', 'None'),
        ('F', 'Following'),
    ]
    status = models.CharField(choices=statusChoices, max_length=15)
    date = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.follower,"->",self.followed}'

class Activity(models.Model):
    a_id = models.CharField(max_length=225)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    location = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Activities"

class Verify(models.Model):
    time_verified = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
class Logged_in(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)
    time_active = models.CharField(max_length=50)
class Security(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    acc_type = models.BooleanField(default=0)
    two_ver = models.BooleanField(default=0)
    sec_question = [
    ('MN', 'What is your middle name?'),
    ('FF', 'What is your favourite food?'),
    ('FW', 'What is your favourite day of the week?'),
    ('FN', 'What is your first Nickname?'),
    ('PN', "What is your pet's name?"),
    ]
    sec_answer = models.CharField(max_length=50 , choices=sec_question, default="")
#This is useless when you can link it directly to the user model
class Chat_member(models.Model):
    chat_member = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.chat_member}'

class Chat_room(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    members = models.ManyToManyField(User, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_accessed = models.DateTimeField(auto_now=True)
    #chat_type = group or chat
    def __str__(self):
        return f'{self.room_id}'

class Chat_text(models.Model):
    #chat_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True);
    room_id = models.ForeignKey(Chat_room, on_delete=models.CASCADE)
    chat_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    chat_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    text = models.CharField(max_length=225, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Chat Texts"

#Check if a user is typing
class Chat_log(models.Model):
    #event being done
    room_id = models.ForeignKey(Chat_room, on_delete=models.CASCADE, related_name="+")
    #person making event
    event_user = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank = True)
    event_choices = [
        ('N', 'None'),
        ('T', 'Typing'),
    ]
    #event being carried out
    chat_state = models.CharField(
        max_length = 1,
        choices = event_choices,
        blank = False,
        default = "N",
        )
    #time event was carried out
    datetime = models.DateTimeField(auto_now = True)

    def update_datetime(self):
        if timezone.now() >= self.datetime + timedelta(seconds = 10):
            self.chat_state = "N"
            self.save()
    def __str__(self):
        return f'{self.event_user,self.room_id,self.chat_state}'

    class Meta:
        verbose_name_plural = "Chat Logs"