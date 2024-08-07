from django.db import models
import os
# Create your models here.

class Collaboration(models.Model):
    CollabName = models.CharField(max_length = 200,unique=True,null=False,blank=False)
    Admin = models.CharField(max_length=200 , null=False)
    CreationTime = models.DateTimeField(auto_now_add=True)

class CollabMembers(models.Model):
    CollabName = models.ForeignKey(Collaboration,on_delete=models.CASCADE)
    CollabMembers = models.CharField(max_length=200,null=False)
    JoinTime = models.DateTimeField(auto_now_add=True)
    
class CollabData (models.Model):
    CollabName = models.ForeignKey(Collaboration,on_delete=models.CASCADE)
    MemberName = models.CharField(max_length=200,null=False)
    SharingTime = models.DateTimeField(auto_now_add=True)
    DataType = models.CharField(max_length=10)
    Link = models.FileField(upload_to="uploads/collab",null=True,blank=True)
    Data = models.CharField(null=True,max_length=1000,blank=True)
    Comment = models.CharField(max_length=200,null=True,blank=True)
    def delete(self, *args, **kwargs):
        if self.Link:
            if os.path.isfile(self.Link.path):
                os.remove(self.Link.path)
        super().delete(*args, **kwargs)

class CollabMessages(models.Model):
    CollabName = models.ForeignKey(Collaboration,on_delete=models.CASCADE)
    MemberName = models.CharField(max_length=200,null=False)
    Message = models.CharField(max_length=1000,null=False)
    MessageTime = models.DateTimeField(auto_now_add=True)

