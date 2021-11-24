from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description  = TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
          order_with_respect_to = 'user'

    def __str__(self):
        return self.title
