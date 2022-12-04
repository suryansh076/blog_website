from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.utils.html import format_html
from .helper import *


# Create your models here.      
class BlogModel(models.Model):
    title=models.CharField(max_length=100)
    content = FroalaField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=1000,null=True, blank=True)
    image=models.ImageField(upload_to='blog')
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def image_tag(self):
        return format_html('<image src="/media/{}" style="width:40px;height:40px; border-radius:50%;"/>'.format(self.image))

    def save(self, *args, **kwargs):
            self.slug = generate_slug(self.title)
            super(BlogModel, self).save(*args, **kwargs)


class profile(models.Model):
    user_name=models.OneToOneField(User,on_delete=models.CASCADE)
    pro_img=models.ImageField(upload_to='profile', default='default.jpg')
    token=models.CharField(max_length=150)
    join=models.DateTimeField(auto_now=True)
    verify=models.BooleanField(default=False)
    block=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user_name)
    def image_tag(self):
            return format_html('<image src="/media/{}" style="width:40px;height:40px; border-radius:50%;"/>'.format(self.pro_img))