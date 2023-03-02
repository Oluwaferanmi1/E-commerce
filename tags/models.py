from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length= 255)

class TaggedItem(models.Model):  #what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete= models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete= models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
#to create a generic way to identify an object
#  1. Type of the object (product, video)
# 2. ID of the object    
#using content types we can create generic relationships within our models
# to define a generic relationship, there are 3 thing to look out for
#content type, object_id and content object
#ContentType is strictly allowed for generic relationships
#content_type to identify the type of object the user likes
#object_id to refernce the particular object 
#content_object for reading an object





# Create your models here.
