from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name='sender')
    reciver = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name='reciver')
    subject = models.CharField(max_length=60)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)
    