from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ngettext_lazy

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# You can now reference the User model with either get_user_model() or settings.AUTH_USER_MODEL. 
# Refer to Referencing the User model from the official docs for more info.

# Also, when you create a superuser, you should be prompted to enter an email rather than a username