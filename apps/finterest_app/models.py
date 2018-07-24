from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Address(models.Model):
    street_address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    zip_code = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    user_image = models.ImageField()
    bio = models.TextField()
    address_id = models.ForeignKey(Address, related_name = "user_id")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Favorite(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    favorite_image = models.ImageField()
    address_id = models.OneToOneField(Address, related_name = "favorite_id")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    user_id = models.ForeignKey(User, related_name = "comments")
    favorite_id = models.ForeignKey(Favorite, related_name = "comments")
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name = "following")
    followed = models.ForeignKey(User, related_name = "followed_by")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)