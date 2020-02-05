from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    @property
    def fullname(self):
        return self.get_full_name() if self.first_name and self.last_name else self.username

    def __str__(self):
        return self.fullname
