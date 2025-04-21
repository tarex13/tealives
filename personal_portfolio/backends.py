from django.contrib.auth.backends import ModelBackend
from django.core.validators import validate_email
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

class BasicBackend:
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class EmailBackend(BasicBackend):
    def authenticate(self, request, username=None, password=None):
        #If username is an email address, then try to pull it up
        try:
            validate_email(username)
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None
        except:
            #We have a non-email address username we should try username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        if user.check_password(password):
            return user