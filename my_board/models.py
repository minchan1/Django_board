from django.db import models

# Create your models here.
# ORM (Object Relation Mapping)

class board( models.Model ):
    createDate = models.DateField()
    writer = models.CharField(max_length=128)
    subject = models.CharField(max_length=255)
    content = models.TextField()