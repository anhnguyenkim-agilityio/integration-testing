# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=255)
    sound = models.CharField(max_length=255)
    # color = models.CharField(max_length=255)
