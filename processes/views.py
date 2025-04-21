from copyreg import dispatch_table
from pickle import FALSE, TRUE
from urllib.request import CacheFTPHandler
import uuid
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from tealives.models import Post, Story, Comments, Activity, Follower_followed, Files, Chat_room, Chat_text, Chat_log, Post_likes
import datetime
from django.http import HttpResponse,HttpRequest
import os
from django.http import Http404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
import json
from itertools import chain
from django.db.models import Q
from django.db.models import F

try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

# Create your views here.
def post_index(request):
    if request.user.is_authenticated:
        if request:
            username = User.objects.all().get(username=request.user)
            if (Follower_followed.objects.all().filter(follower = username)):
                followed = Follower_followed.objects.all().filter(follower = username) # The people I followed
                post = Post.objects.filter(username__user_id__in = followed.values('followed'))
                recommended = False
            else:
                post = Post.objects.all()
                recommended = True

    #Enumerate allows us to use the index like in js
            post_ = list(post.values("p_id","username__username","username__display_picture__uploadedFile","title","top_text","desc","created_on","location","alt_text","desc", "files__uploadedFile", "template"))
            for index,x in enumerate(post):
                liked = Post_likes.objects.filter(Q(post__p_id=post_[index]["p_id"])&Q(user=request.user,status="L"))
                if liked:
                    post_[index]['isLiked']=True
                else:
                    post_[index]['isLiked']=False
                post_[index]['likes']=(x.likes())
                post_[index]['comments']=(x.comments())
                #data.append(post_)
                #post_list += data
            #html[0]['recommended'] = recommended
            user_agent = request.META['HTTP_USER_AGENT']
            return JsonResponse(post_, safe=False)
        else:
            return redirect('lin')
def post_comment(request,p_id):
    if request.user.is_authenticated:
        if request.method == "GET":
            comment = Comments.objects.filter(c_post=p_id).values("c_comment_text", "c_modified", "c_sender_id", "c_sender_id__username")
            html = list(comment)
            return JsonResponse(html, safe=False)
        elif request.method == "POST":
            try:
                text = request.GET.get("ct")
                post = get_object_or_404(Post, p_id=p_id)
                comment = Comments(
                    c_post = post,
                    c_sender = User.objects.get(username=request.user.username),
                    c_receiver = User.objects.get(username=post.username),
                    c_comment_text = text,
                    )
                comment.save()
                    #sender = request.POST.get('')
                    #receiver = request.POST.get('')
                    #post_id = request.POST.get('')
                    #text = request.POST.get('')
                    #time = request.POST.get        
                return JsonResponse({"status": "success"}, safe=False)
            except:
                return JsonResponse({"status": "failed"}, safe=False)

    else:
        return redirect('lin')
def user_details(request):
    if request.user.is_authenticated:
            if request.method == "GET":
                user = User.objects.all().filter(username=request.user).values('username','email','first_name','last_name','bio','gender','dob','p_no', 'dob')
                print(request.META.get('HTTP_X_REQUESTED_WITH'))
                user_list = list(user)
                return JsonResponse(user_list, safe=False)

    else:
        messages.info(request, 'Username OR password is incorrect')
        return redirect('lin')

    # posts = Post.objects.all().filter().order_by("-created_on")
    # admin = Adminpost.objects.all().order_by("-created_on")
    # post = Post.objects.all()
    # categories = Category.objects.all()
    # user = User.objects.all()
    # year = datetime.date.today().year
    # BASE_DIR = "http://localhost:8000/tea_media/media/"
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
def user_search(request):
    if request.method == "GET":
        q = request.GET.get("q")#Query
        src = request.GET.get("src")#Source Page
        lg = request.GET.get("lang")#Language
        ip = request.GET.get("ipd")#IP Address
        client = request.GET.get("client")#Search client which is tealives
        suggestions = []
        if q:
            #Sign up page
            if src == "s_u_p":
                try: 
                    User.objects.all().get(username=q)
                    result = {
                        "uname":q,#q = query
                        "result":"Username already exists!",
                        "src":"S_U_P",
                        "cln":client,
                        "ipd":ip,
                        "lang":lg,
                        "return":False,
                    }
                except:
                    result = {
                        "result":"Username is available!",
                        "uname":q,
                        "src":"S_U_P",
                        "cln":client,
                        "ipd":ip,
                        "lang":lg,
                        "return":True,
                    }
                user = [result]
                user_list = list(user)
                html = json.dumps(result)
                return JsonResponse(user, safe=False)
            # Home Page
            elif src == "teabase":
                user = User.objects.all().filter(Q(username__contains=q)|Q(first_name__contains=q)|Q(last_name__contains=q)).values("username", "first_name", "last_name")
                users = list(user)
                return JsonResponse(users, safe=False)
            else:
                print("hi")
                return redirect('lin')
        else:
            print("hi2")
            return redirect('lin')
        
    else:
        print("hi3")
        return redirect('lin')

def story_get(request, user_id, ref, story_owner):
    story = Story.objects.filter(story_id = story_owner).values("user__user_id", "story_id","file__name","file__file_type","text")
    #Story.objects.all().filter(username = user_id).values('')
    stories = list(story)
    return JsonResponse(stories, safe=False)

def following_stories(request):
    user = User.objects.all().get(username=request.user)
    followed = Follower_followed.objects.all().filter(follower = user) # The people I followed
    if followed.exists():
        story_user = Story.objects.filter(user = request.user)
        story_followed = Story.objects.filter(user = followed).values("user__user_id", "story_id","file__name","file__file_type","text")
        stories = list(story_user,story_followed)
        return JsonResponse(stories, safe=False)
    else:
        return get_object_or_404(followed)
    
def chat_pc(request, chat_room):
    if request.method == "GET":
        chat = Chat_text.objects.filter(room_id = chat_room).values('chat_from__username', 'chat_to__username', 'text').order_by("created_on")
        html = list(chat)
        return JsonResponse(html, safe=False)
    elif request.method == "POST":
        chatFrom = request.GET.get("cfr")
        chatTo = request.GET.get("cto")
        text = request.GET.get("text")
        chat = Chat_text(
            room_id = Chat_room.objects.get(room_id = chat_room),
            chat_from = User.objects.get(user_id = chatFrom),
            chat_to = User.objects.get(user_id = chatTo),
            text = text
            )
        try:
            chat.save()
            return JsonResponse("success", safe=False)
        except:
            return JsonResponse("failed", safe=False)
    #r and pk are the same do sth bout it
    #let everyone get their own chat log instead of two people sharing one
#def get_chatrooms(request):
#    if request.method == "GET":
#        chat_rooms = Chat_room.objects.filter(members__chat_member__username = request.user.username).values("room_id")
#        chatty = Chat_room.objects.filter(room_id__in = chat_rooms).values("members__chat_member__username")
#        user = User.objects.filter(username__in=chatty).exclude(username=request.user.username).values()
#        chat_room_list = list(chat_rooms)
#        contact_user_list = list(user)
#        return JsonResponse(chat_room_list+contact_user_list, safe=False)

def chat_profile(request, username):
    if request.method == "POST":
        chatFrom = request.user
        chatTo = request.GET.get("cto")
        text = request.GET.get("text")
        
        room = Chat_room.objects.get(Q(members__username = chatFrom),  Q(members__username = chatFrom))
        
            
        chat = Chat_text(
            room_id = Chat_room.objects.get(room_id = room.room_id),
            chat_from = User.objects.get(user_id = chatFrom.pk),
            chat_to = User.objects.get(username = chatTo),
            text = text
            )

        try:
            chat.save()
            return JsonResponse("success", safe=False)
        except:
            return JsonResponse("failed", safe=False)
            
def get_chatrooms(request):
    if request.method == "GET":
        chat_rooms = Chat_room.objects.filter(members__username = request.user.username).values("room_id")
        chat_room_list = list()
        data = []
        me = 0
        for x in chat_rooms:
            me+=1;
            chatty = Chat_room.objects.filter(room_id = x["room_id"]).values("members__username")
            user = User.objects.filter(username__in=chatty).exclude(username=request.user.username).values("username", "display_picture__uploadedFile", "first_name", "last_name")
            lastChat = Chat_text.objects.filter(room_id=x["room_id"]).last()
            if lastChat:
                lastChat = lastChat.text
            else:
                lastChat = ""
            data.clear()
            data.append({'room':{"id":x,'message':lastChat},'user':list(user)})
            chat_room_list += list(data)
        return JsonResponse(chat_room_list, safe=False)

def user_relations(request):
    if request.method == "GET":
        #Status = independent?
        if request.GET.get("s")=="i":
            users = str(request.GET.get("u")).split("-;-")
            try:
                user_followed = User.objects.all().get(username=users[0])#The person following
                user_follower = User.objects.all().get(username=users[1])#The person following
                try:
                    followed = Follower_followed.objects.filter(follower = user_follower).get(followed=user_followed)
                    print(followed.status)
                    if(followed.status=="F"):
                        followed.status = "N"
                    else:
                        followed.status = "F"
                    followed.save()
                except:
                    print(users[1])
                    relation = Follower_followed(
                        follower = user_follower,
                        followed = user_followed,
                        status = "F",
                        )
                    relation.save()
                list = {"status": "success"}
            except:
                list = {"status": "failed"}
           
        
            return JsonResponse(list, safe=False)

def chat_log(request,pk):
    if request.method == "POST":
        room = request.GET.get("r")
        #User Id and name
        user_complete = str(request.GET.get("u"))
        print(user_complete)
        #User split
        user = user_complete.split("-;-")
        user_id = user[0]
        user_name = user[1]
        status = request.GET.get('status')
        if status == 't':
            status = "T"
        elif status == 'n':
            status = "N"
        try:
            #Does not work
            #log = Chat_log.objects.filter(room_id__room_id = str(room)).update(room_id__room_id = F(room), event_user__username = F(user_name), chat_state = F(status))
            log = Chat_log.objects.get(room_id__room_id = str(room), event_user__username = user_name)
            log.room_id__room_id = room,
            log.event_user__username = user_name,
            log.chat_state = status
        except:
            log = Chat_log(
                room_id = Chat_room.objects.get(room_id = room),
                event_user = User.objects.get(username = user_name),
                chat_state = status
                )
        try :
            log.save()
            return JsonResponse("success", safe=False)
        except:
            return JsonResponse("failed", safe=False)
    elif request.method == "GET":
        # Get friend's log
        cfr = request.GET.get("cfr")
        cfr_ = User.objects.get(user_id = cfr)
        #Has to be get to update
        #log = Chat_log.objects.filter(room_id__room_id = pk, event_user = cfr)
        #log.update()
        try:
            log = Chat_log.objects.get(room_id__room_id = pk, event_user = cfr)
        except:
            room = Chat_room.objects.get(members__user_id = cfr)

            print(room)
            log = Chat_log.objects.create(room_id = room, event_user = cfr_)
            log.save()
        log.update_datetime()
        log = Chat_log.objects.filter(room_id__room_id = pk, event_user = cfr).values('room_id','event_user','chat_state')
        log = list(log)
        return JsonResponse(log, safe=False)

def post_like(request, post_id):
    try:
        post = get_object_or_404(Post,p_id = post_id)
    
        try:
            like = Post_likes.objects.get(post=post, user=request.user)
            #L = Like
            #U = Unlike
            if like.status == "L":
                like.status = "U"
            else:
                like.status = "L"
            like.save()
        except:
            like = Post_likes(
                user = request.user,
                post = post,
                status = "L"
                )
            like.save()
        return JsonResponse({"status": "success", "r":like.status}, safe=False)
    except:
        return JsonResponse({"status": "failed"}, safe=False)
