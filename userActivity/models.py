# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.template.defaultfilters import slugify
import random
import string
from timezone_field import TimeZoneFormField

from .managers import CustomUserManager

class FTUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    uid = models.SlugField(null=False, blank=True, max_length=100)
    real_name = models.CharField(null=True, blank=True, max_length=100)
    tz = models.CharField(max_length=100, blank=True, null=True, default='Asia/Kolkata')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.generate_uid()
        super(FTUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.real_name

    def generate_uid(self):
        if not self.uid:
            self.uid = slugify(str(self.real_name.split("@")[0]) + "-" + ''.join(
                random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
