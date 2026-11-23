from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.text import slugify
import re

# Create your models here.
class Blog(models.Model):
   id=models.UUIDField(primary_key=True,default=uuid.uuid4,)
   slug_field=models.SlugField(max_length=200,unique=True)
   title=models.CharField(max_length=100)
   description=models.TextField()
   user=models.ForeignKey(User,on_delete=models.CASCADE)

   def save(self,*args,**kwargs):
      if not self.slug_field:
         clean_title=re.sub(r'[^\w\s\u0980-\u09FF-]','', self.title).strip()
         base_slug = re.sub(r'[-\s]+','-',clean_title)
         unique_part = str(uuid.uuid4())[:6]
         self.slug_field = f"{base_slug}-{unique_part}" if base_slug else unique_part
      super().save(*args, **kwargs)

   def __str__(self):
      return self.title