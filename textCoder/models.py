# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CodingElement(models.Model):
    textEntered = models.CharField(max_length=1000,null=True)
    textEncoded = models.CharField(max_length=1000,null=True)
    rails = models.IntegerField()
    username = models.CharField(max_length=100, default='GuestName')
    
    def __str__ (self):
        return self.textEntered
