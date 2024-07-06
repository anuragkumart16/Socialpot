from django.db import models
import os
from django.contrib.auth.models import User
# Create your models here.
class Linkmodel(models.Model):
    Link = models.TextField(max_length=10000)
    user = models.CharField(max_length=200)

    

class Textmodel(models.Model):
    Text = models.TextField(max_length=1000)
    user = models.CharField(max_length=100,null=False)

class Filemodel(models.Model):
    File = models.FileField(upload_to="uploads/")
    Filename=models.CharField(max_length=200,default=None,null=True)
    user_obj = models.CharField(max_length=100,null=False)
    def delete(self, *args, **kwargs):
        # Delete the file from the filesystem
        if self.File:
            if os.path.isfile(self.File.path):
                os.remove(self.File.path)
        super().delete(*args, **kwargs)
