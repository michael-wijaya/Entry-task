from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#from django.contrib.auth.models import User
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

