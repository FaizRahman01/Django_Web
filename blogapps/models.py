from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class UserPost (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True) # null/blank = True will set form input to not required
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    #return username title desc id
    def __str__(self):
        return self.title