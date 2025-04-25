from ast import Not
import datetime
from pickle import FALSE
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
#from django.contrib.sites.shortcuts import get_current_site
#from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
#from django.contrib.auth.models import User as auth_user
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
#from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
#from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from .forms import SignUpForm, LoginForm  
#from .token import account_activation_token  
from django.contrib.auth.decorators import login_required
#from django.core.mail import EmailMessage  


# Create your views here.
    

UserModel = get_user_model()

try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()
# Create your views here.
def login(request):
    year = datetime.date.today().year
    home = "127.0.0.1:8000"
    home_name = "Home"
    #username = "tarex_13"
    loginform = LoginForm
    next_ = request.GET.get("next")


    if request.method == "POST":
        if (loginform):
            loginform = LoginForm(request.POST)
            if (loginform.is_valid()):
                cd = loginform.cleaned_data
                user = authenticate(username=cd['userid'], password=cd['userpass'])
                if (user is not None):
                    #Doesnt work
                    if(next_):
                        return redirect(request.GET.get("next"))
                    if not(user.is_disabled):
                        theuser = User.objects.get(username=user)
                        if not(user.is_active):
                            theuser.is_active = True
                            theuser.save()
                        theuser.is_logged_in = True
                        theuser.last_login = request.POST.get('date')
                        if 'user-agent' in request.headers:
                            user_agent = request.headers['User-Agent']
                        else:
                            user_agent = request.META['user_agent']
                        theuser.user_agent = user_agent
                        theuser.save()
                        auth_login(request, user)
                        return redirect('/')
                else:
                    messages.info(request, 'Username OR password is incorrect')
                    return redirect('/')
    


    if request.user.is_authenticated:
        context = {}#"yearr": year, "home": home, "h_name": home_name, "username": username
        return render(request, "nice.html", context)
    else:
        #context = {"yearr": year, "loginform": loginform, "regform": regform}
        context = {"yearr": year, "loginform": loginform}
        return render(request, "lin.html", context)

def signup(request):   
    year = datetime.date.today().year 
    if request.method == 'POST':  
        regform = SignUpForm()
        if(regform):
            regform = SignUpForm(request.POST)
            if (regform.is_valid()):
                reg = regform.cleaned_data
                registration = User(
                    username = reg['username'],
                    email = reg['email'],
                    password = reg['password'],
                    is_logged_in = True,
                    is_disabled = False,
                    is_active = True,
                    )
                registration.set_password(registration.password)
                registration.save()
                print(registration.username,registration.password)
                user = authenticate(username=reg['username'], password=reg['password'])
                if (user is not None):
                    if (user.is_active):
                        auth_login(request, user)
                        return redirect('editAccount')
                else:
                    messages.info(request, 'Username OR password is incorrect')
                    return redirect('/')

        #uname = request.GET.get('uname')
        #email = request.GET.get('email')
        #upass = request.GET.get('pass')

        #user = auth_user()
        #user.objects.create(username = uname,email = email,password = upass)
        #user.set_password(user.password)
         
        

        #user.save()

        #if form.is_valid():  
        #    form =  form.cleaned_data
           
        #    # save form in the memory not in database  
        #    user = form.save(commit=False)  
        #    user.is_active = False  
        #    print(user)
        #    user.save()  
        #    # to get the domain of the current site  
        #    current_site = get_current_site(request)  
        #    mail_subject = 'Activation link has been sent to your email id'  
        #    message = render_to_string('acc_active_email.html', {  
        #        'user': user,  
        #        'domain': current_site.domain,  
        #        'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
        #        'token':account_activation_token.make_token(user),  
        #    })  
        #    to_email = form.cleaned_data.get('email')  
        #    email = EmailMessage(  
        #                mail_subject, message, to=[to_email]  
        #    )  
        #    email.send()  
        #    return HttpResponse('Please confirm your email address to complete the registration')  
        #else:
        #    print("form is invalid")
    else:  
        regform = SignUpForm()  
    return render(request, 'sup2.html', {"yearr": year, "regform": regform})


#def activate(request, uidb64, token):  
#    User = get_user_model()  
#    try:  
#        uid = force_str(urlsafe_base64_decode(uidb64))  
#        user = User.objects.get(pk=uid)  
#    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
#        user = None  
#    if user is not None and account_activation_token.check_token(user, token):  
#        user.is_active = True  
#        user.save()  
#        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
#    else:  
#        return HttpResponse('Activation link is invalid!')  


@login_required(redirect_field_name='next', login_url='lin')
def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return HttpResponseRedirect(reverse('lin'))


#Disable account view
def disable(request):
    if request.method=="POST":
        db_user = User.objects.all().get(username=request.user)
        password = request.POST.get("password")
        if db_user.check_password(password):
            db_user.is_active=False
            db_user.save()
            messages.success(request, 'Your account has been disabled')
            logout(request)
            return redirect('lin')
    context = {}
    return render(request, "disableAccount.html", context)