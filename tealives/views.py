from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponse
import datetime
from tealives.models import Post, Follower_followed
#from tealives.forms import LoginForm
#from tealives.forms import RegistrationForm
from tealives.models import Chat_room
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from tealives.models import Chat_text
'''from django.conf import settings

auth_user = settings.AUTH_USER_MODEL
User = settings.AUTH_USER_MODEL'''
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()
# Create your views here.
#def lin(request):
#    year = datetime.date.today().year
#    home = "127.0.0.1:8000"
#    home_name = "Home"
#    username = "tarex_13"
#    loginform = LoginForm()
#    #regform = RegistrationForm()
#    if request.method == "POST":
#        if (loginform):
#            loginform = LoginForm(request.POST)
#            if (loginform.is_valid()):
#                cd = loginform.cleaned_data
#                user = authenticate(username=cd['userid'], password=cd['userpass'])
#                if (user is not None):
#                    if (user.is_active):
#                        theuser = User.objects.get(username=user)
#                        theuser.is_logged_in = True
#                        theuser.last_login = request.POST.get('date')
#                        if 'user-agent' in request.headers:
#                            user_agent = request.headers['User-Agent']
#                        else:
#                            user_agent = reuest.META['user_agent']
#                        theuser.user_agent = user_agent
#                        theuser.save()
#                        login(request, user)
#                        return redirect('/')
#                else:
#                    messages.info(request, 'Username OR password is incorrect')
#                    return redirect('/')
#        elif(regform):
#            regform = RegistrationForm(request.POST)
#            if (regform.is_valid()):
#                reg = regform.cleaned_data
#                registration = User(
#                    username = reg['username'],
#                    is_logged_in = True,
#                    is_disabled = False,
#                    )
#                registration.save()
#                if (user is not None):
#                    if (user.is_active):
#                        login(request, user)
#                        return redirect('/')
#                else:
#                    messages.info(request, 'Username OR password is incorrect')
#                    return redirect('/')

#    if request.user.is_authenticated:
#        context = {}#"yearr": year, "home": home, "h_name": home_name, "username": username
#        return render(request, "nice.html", context)
#    else:
#        context = {"yearr": year, "loginform": loginform, "regform": regform}
#        return render(request, "lin.html", context)
    
def fp(request):
    context = {}
    return render(request, "fp.html", context)
def settings(request):
    context = {}
    return render(request, "inn.html", context)
def dm(request):
    # Open means that no user has been clicked
    context = {'page': "open"}
    return render(request, "extra.html", context)
def dm_room(request, chat_room):
    if request.user.is_authenticated:
        chat = Chat_room.objects.get(room_id = chat_room)
        print(chat.members)
        #user = Chat_text.objects.filter(room_id = chat.room_id)[0]
        members = chat.members.all()
        if (members[0].user_id == request.user.user_id):
            friend = members[1]
        else:
            friend = members[0]
            #Room means that a user chat has been clicked
        context = {"room": chat, "friend_id": friend.user_id,"friend_name": friend.username, "me_id": request.user.user_id, "me_name": request.user.username, 'page': "room"}
    else:
        return redirect('lin')
    return render(request, "extra.html", context)
@login_required(redirect_field_name='next', login_url='lin')
def edit(request):
    if request.method == "POST":
        db_user = User.objects.all().get(username=request.user)
        db_user.username = request.POST.get('username')
        db_user.email = request.POST.get('email')
        db_user.first_name = request.POST.get('f_name')
        db_user.last_name = request.POST.get('l_name')
        db_user.dob = request.POST.get('dob')
        db_user.p_no = request.POST.get('p_no')
        db_user.bio = request.POST.get('bio')
       # db_user.url = request.POST.get('web')
        db_user.dob = request.POST.get('dob')
        db_user.user_agent = request.META['HTTP_USER_AGENT']
        gender = request.POST.get('gend')
        if gender == "Male":
            db_user.gender = "M"
        elif gender == "Female":
            db_user.gender = "F"
        elif gender == "Others":
            db_user.gender = "O"
        try:
            db_user.save()
            messages.success(request, 'User profile updated successfully!','success')
        except:
            messages.error(request, 'An error was encountered. Try again!','error')

    context = {}
    return render(request, "editProfile.html", context)
@login_required(redirect_field_name='next', login_url='lin')
def acc_activity(request):
    db_user = User.objects.all().get(username=request.user)
    context = {"user":db_user}
    return render(request, "acc_activity.html", context)

@login_required(redirect_field_name='next', login_url='lin')
def changePass(request):
    if request.method == "POST":
        oldP = request.POST.get('19iuw')
        newPass1 = request.POST.get('19iua')
        newPass2 = request.POST.get('19iub')
        if newPass1 == newPass2:
            newPass = newPass1
        else:
            messages.error(request, 'New Passwords don\'t match!','error')
        user = get_object_or_404(User, username = request.user.username)
        if user.check_password(oldP):
            user.set_password(newPass)
            user.save()
        else:
            messages.error(request, 'Password is incorrect!','error')
    context = {}
    return render(request, "passworddoc.html", context)
def accountsec(request):
    context = {}
    return render(request, "accountSecurity.html", context)
def pref(request):
    context = {}
    return render(request, "pref.html", context)
def events(request):
    context = {}
    return render(request, "events.html", context)
def aboutUser(request, username2):
    context = {}
    return render(request, "aboutPage.html", context)
def profile(request,username):
    try:
        db_user = User.objects.all().get(username=username)
        pLen = Post.objects.all().filter(username=db_user.user_id).count()
        
        # username = db_user.username
        # f_name = db_user.first_name + "" + db_user.last_name 
        # bio = db_user.bio
        # url = db_user.url
        # People I follow
        fdLen = Follower_followed.objects.filter(follower = db_user).count()
        # People that follow me
        frLen = Follower_followed.objects.filter(followed = db_user).count()
        if db_user.username != request.user.get_username:
            try:
                following = Follower_followed.objects.get(follower = request.user, followed=db_user, status="F")
                following = True
            except:
                following = False
        context = {'db':db_user, 'pLen':pLen, 'fdLen': fdLen, 'frLen': frLen, 'following': following}
        return render(request, "profile.html", context)
    except:
        raise Http404
def aboutPage(request,username):
    try:
        db_user = User.objects.all().get(username=username)
        pLen = Post.objects.all().filter(username=db_user.user_id).count()
        
        # username = db_user.username
        # f_name = db_user.first_name + "" + db_user.last_name 
        # bio = db_user.bio
        # url = db_user.url
        # People I follow
        fdLen = Follower_followed.objects.filter(follower = db_user).count()
        # People that follow me
        frLen = Follower_followed.objects.filter(followed = db_user).count()
        context = {'db':db_user, 'pLen':pLen, 'fdLen': fdLen, 'frLen': frLen}
        return render(request, "aboutPage2.html", context)
    except:
        raise Http404
@login_required(redirect_field_name='next', login_url='lin')
def create(request):
    context = {}
    # db_user = 
    return render(request, "post_create.html", context)
def lin2(request):
    year = datetime.date.today().year
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if (form.is_valid()):
            cd = form.cleaned_data
            user = authenticate(username=cd['userid'], password=cd['userpass'])
            if (user is not None):
                if (user.is_active):
                    login(request, user)
                    return redirect(lin)
            else:
                messages.info(request, 'Username OR password is incorrect')
                redirect('lin2')

    context = {"yearr": year, "form": form}
    return render(request, "lin2.html", context)
