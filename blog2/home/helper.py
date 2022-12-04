
from django.utils.text import slugify
import string
import random
 
def rand_str(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))
    return res
 

def generate_slug(text):
    from .models import BlogModel
    new_slug=slugify(text)
    print(new_slug)
    if BlogModel.objects.filter(slug=new_slug).first():
        new_slug= generate_slug(text+'-'+ rand_str(5))
    return new_slug


