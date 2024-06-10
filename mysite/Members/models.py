from django.db import models
import os
# Create your models here.
class ToolModel(models.Model):
    ToolName = models.CharField( max_length=50,null=False)
    ToolDescription = models.CharField(max_length=500,null=False)
    Image = models.FileField(upload_to="uploads/",null=False)
    Urlpattern = models.CharField(max_length=100, null=False,default="null")
    def delete(self, *args, **kwargs):
        # Delete the file from the filesystem
        if self.File:
            if os.path.isfile(self.File.path):
                os.remove(self.File.path)
        super().delete(*args, **kwargs)
