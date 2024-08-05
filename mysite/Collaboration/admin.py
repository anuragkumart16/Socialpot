from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Collaboration)
admin.site.register(CollabMessages)
admin.site.register(CollabMembers)
admin.site.register(CollabData)