from django.db import models
import os

# Create your models here.
class Linkmodel(models.Model):
    Link = models.TextField(max_length=500)
    user_obj = models.CharField(max_length=100,default='none')

class Textmodel(models.Model):
    Text = models.TextField(max_length=1000)
    user_obj = models.CharField(max_length=100,default='none')

class Filemodel(models.Model):
    File = models.FileField(upload_to="uploads/")
    Filename=models.CharField(max_length=200,default=None)
    user_obj = models.CharField(max_length=100,default='none')
    def delete(self, *args, **kwargs):
        # Delete the file from the filesystem
        if self.File:
            if os.path.isfile(self.File.path):
                os.remove(self.File.path)
        super().delete(*args, **kwargs)
