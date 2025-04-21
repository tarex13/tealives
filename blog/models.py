from django.db import models
import datetime
from django.utils import timezone
#from ads.models import

class Category(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    path = models.CharField(max_length=200, default="")
    #pic = models.FilePathField(path="c:/",allow_files=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    #followers =  models.IntegerField()
    user = models.ManyToManyField("User", related_name="posts")
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_on <= now

    was_published_recently.admin_order_field = 'created_on'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

class Adminpost(models.Model):
    author = models.CharField(max_length=255, default="Tealives")
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255, default="")
    pre_body = models.CharField(max_length=255, default="")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, null=False)
    #pic = models.FilePathField(path="c:/",allow_files=True)
    #categories = models.ManyToManyField("Category", related_name="adpost")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_on <= now

    was_published_recently.admin_order_field = 'created_on'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.heading

class User(models.Model):
     name = models.CharField(max_length=255)
     username = models.CharField(max_length=255)
     email = models.EmailField(unique=True)
     country = models.CharField(max_length=255)
     password = models.CharField(max_length=255)
     dob = models.DateField(auto_now=False)
     pic = models.CharField(max_length=255)
     followers = models.IntegerField()
     created_on = models.DateTimeField(auto_now_add=True)
     last_modified = models.DateTimeField(auto_now=True)

     def __str__(self):
         return self.name

#class Comment(models.Model):
    #sender_from = models.ForeignKey("User", on_delete=models.CASCADE)
    #receiver_t0 = models.ForeignKey("User", on_delete=models.CASCADE)
    #created_on = models.DateTimeField(auto_now_add=True)