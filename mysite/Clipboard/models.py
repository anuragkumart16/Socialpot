from django.db import models
import os

# Create your models here.
class Linkmodel(models.Model):
    Link = models.TextField(max_length=500,unique=True)

class Textmodel(models.Model):
    Text = models.TextField(max_length=1000,unique=True)

class Filemodel(models.Model):
    File = models.FileField(upload_to="uploads/")
    def delete(self, *args, **kwargs):
        # Delete the file from the filesystem
        if self.File:
            if os.path.isfile(self.File.path):
                os.remove(self.File.path)
        super().delete(*args, **kwargs)
