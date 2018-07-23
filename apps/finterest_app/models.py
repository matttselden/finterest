from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData["first_name"])<2:
            errors["first_name"] = "First Name must have no fewer than 2 characters."
        if postData["first_name"].isalpha() == False:
            errors["first_name_a"] = "First Name should only contain letters."
        if len(postData["last_name"])<2:
            errors["last_name"] = "Last Name must have no fewer than 2 characters"
        if postData["last_name"].isalpha() == False:
            errors["last_name_a"] = "Last Name should only contain letters."
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid Email Address"
        if postData["password"] != postData["confirm"]:
            errors["password"] = "Passwords must match"
        if len(postData["password"])<8:
            errors["password_l"] = "Password must have no fewer than 8 characters."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()