from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # first name validators
        if len(postData['first_name']) < 2:
            errors["first_name"] = "We need your first name please"
        elif not str.isalpha(postData['first_name']): 
            errors["first_name_letter"] = "Your first name can only consist of letters"    
        # last name validators
        if len(postData['last_name']) < 2:
            errors["last_name"] = "We need your last name please"
        elif not str.isalpha(postData['last_name']): 
            errors["last_name_letter"] = "Your last name can only consist of letters"     
        # email validators
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_regex'] = "Please submit a valid email address"
        users_list = User.objects.filter(email= postData['email'])
        if len(users_list) >  0:
            errors["email_unique"] = "Your email is already in use"
        # password validators
        if len(postData['password']) < 8:
            errors["password"] = "Your password needs to be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors["password"] = "Your passwords do not match"
             
        return errors

    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors["logine"] = "Please enter your email"
        if len(postData['password']) < 1:
            errors['loginp'] = "Please enter your password"  
        else: 
            users_list = User.objects.filter(email= postData['email'])
            if (len(users_list) <  1) or not (bcrypt.checkpw(postData['password'].encode(), users_list[0].password.encode())):    
                errors["loginp"] = "Your password or email is not correct"
        return errors


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
    user_image = models.ImageField(blank=True, upload_to='profile_image/')
    bio = models.TextField(null=True)
    address_id = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name = "user_id")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


class Favorite(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    favorite_image = models.ImageField(blank=True, upload_to='favorite_image/')
    address_id = models.OneToOneField(Address, related_name = "favorite_id")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name = "comments")
    favorite_id = models.ForeignKey(Favorite, on_delete=models.DO_NOTHING, related_name = "comments")
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name = "following")
    followed = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name = "followed_by")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)