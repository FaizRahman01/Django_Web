from django.db import models
import uuid
# Create your models here.

class UserPost (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True) # null/blank = True will set form input to not required

    #return username title desc id
    def __str__(self):
        return self.title 