from django.db import models
from login_app.models import User

# Create your models here.

class MessageManager(models.Manager):
    def basic_validator(self, post_data):
        errors ={}
        if len(post_data['message']) < 1 or len(post_data['message']) > 55:
            errors['message'] = 'Message must be between 1-55 characters'
        return errors
    
    

class CommentManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['comment']) < 1 or len(post_data['comment']) > 55:
            errors['comment'] = 'Comment must be between 1-55 characters'
        return errors



class Message(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    content= models.TextField()
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
    