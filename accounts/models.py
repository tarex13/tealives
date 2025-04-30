from email.policy import default
#from msilib.schema import CustomAction
from pickle import FALSE
import uuid
from django.db import models
from tealives.models import Files
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from tealives.models import generate_random_filename
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dob = models.DateField(blank=True, null=True)
    display_picture = models.ForeignKey(Files, on_delete=models.DO_NOTHING, null=True, blank=True)
    country = models.CharField(max_length=255, blank=True)
    user_agent = models.TextField(default="", blank=True)
    user_zone = models.CharField(max_length=255)
    language = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(
        _('Active'),
        default=False
        )
    is_logged_in = models.BooleanField(
        _('Logged In'),
        default=False
        )
    email_confirmed = models.BooleanField(default=False)
    is_verified = models.BooleanField(
        _('Verified'),
        default=False,
        help_text=_(
            'Select if user should be verified. '
        ),
    )
    is_disabled = models.BooleanField(
        _('Disabled'),
        default=False,
        help_text=_(
            'Designates whether this users account should be disabled. '
            'Select this when user violates policy.'
        ),
    )
    #is_suspended
    date_joined = models.DateField(_('Date Joined'), default=timezone.now, editable=False)
    bio = models.TextField(blank=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    p_no = models.CharField(_('Phone Number'), max_length=20, blank=True)
    #url = models.URLField(_(''), default="",blank=True)
    gender=models.CharField(max_length=10, choices=gender_choices, blank=True)
    last_login = models.DateTimeField(_('Last Login'), max_length=50, blank=False, auto_now=True, editable=False)

    def __str__(self):
        return '%s' % (self.username)
    
