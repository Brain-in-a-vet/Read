# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    authorName=models.CharField(max_length=500) 
    authorCode=models.CharField(max_length=500) 
    desc=models.CharField(max_length=5000)
    imgpath=models.CharField(max_length=200)


class NavModel(models.Model):
    navName=models.CharField(max_length=500)
    navCode=models.CharField(max_length=500)
    authorCode=models.CharField(max_length=500) 

class NavItemModel(models.Model):
    itemName=models.CharField(max_length=500)
    itemCode=models.CharField(max_length=500)
    navCode=models.CharField(max_length=500)

class ItemContentModel(models.Model):
    content=models.CharField(max_length=5000)
    itemCode=models.CharField(max_length=500)