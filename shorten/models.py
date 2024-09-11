from django.db import models
import uuid
# Create your models here.


class ShortenUrl(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    originalurl = models.CharField(max_length=100,blank=True,null=True)
    shorturl = models.CharField(max_length=100,blank=True,null=True,unique=True)
    def __str__(self):
        return self.shorturl