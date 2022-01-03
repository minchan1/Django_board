from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# ORM (Object Relation Mapping)

class board( models.Model ):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createDate = models.DateField()
    #writer = models.CharField(max_length=128)
    subject = models.CharField(max_length=255)
    content = models.TextField()

class board_reply( models.Model ):
    user = models.CharField(max_length=128)
    createDate = models.DateField()
    content = models.TextField()