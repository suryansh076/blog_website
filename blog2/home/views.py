import uuid
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from .models import *
from blog2 import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
def send_mail_to_user(request,name,token,user_email):
    subject="Welcome to MY PEN "
    html_content=render_to_string("email_template.html",{'name':name,'path':get_current_site(request),'token':token})
    text_content=strip_tags(html_content)
    email=EmailMultiAlternatives(
        subject,
        text_content,
        settings.EMAIL_HOST_USER,
       [user_email]
    )
    email.attach_alternative(html_content,'text/html')
    email.send(fail_silently=True)
    # send_mail(subject,msg,from_email,to_list,fail_silently=True)
def homes(request):
    context={}
    if request.user.is_authenticated:
        context={}
        print(request.user,"oooooooooooooooooooooooooooooo")
        context['profiles']=profile.objects.filter(user_name=request.user).first()
        context['blog']=BlogModel.objects.all()
    else:
        context['blog']=BlogModel.objects.all()
        


    return render(request,'home.html',context)
def login(request):
    return render(request,'login.html')

def add_blog(request):
    context={'form':Blogform,'profiles':profile.objects.filter(user_name=request.user).first()}
    try:
        if request.method=='POST':
            form=Blogform(request.POST)
            image=request.FILES['image']
            user=request.user
            title=request.POST['title']
            if form.is_valid():
                print("-----------------yes i am in")
                content=form.cleaned_data['content']
                blog_user=BlogModel.objects.create(title=title,user=user,content=content,image=image)
                blog_user.save()
            print(user)
            print(title)
            # image=request.f

    except Exception as e:
        print("add_Blog    ",e)
    return render(request,'add_blog.html',context)

def signup(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass2!=pass1:
            messages.error(request,"Password Must be same")
            return redirect('signup')
        if len(pass1)<6:
            messages.error(request,"password must have at least 6 char's")
            return redirect('signup')
        user=User.objects.filter(username=name).first()
        if user:
            messages.error(request,"User already exist Try with different name")
            return redirect('signup')
        # user_mail=User.objects.filter(email=email).first()
        # if user_mail:
        #     messages.error(request,"This Email Is already in used")
        #     return redirect('signup')
        print(name)
        print(email)
        print(pass1)
        print(pass2)
        try:
            user_create=User.objects.create_user(username=name,email=email,password=pass1)
            user_create.save()
            uid=uuid.uuid4()
            user_profile=profile.objects.create(user_name=user_create,token=uid)
            user_profile.save()
            messages.success(request,"Account created check Email to verify your account")
            send_mail_to_user(request,name,uid,email)
        except Exception as e:
            print(e)
            return render(request,'error.html')
    return render(request,'register.html')

def blog_detail(request,slug):
    context={}
    try:
        blog_obj=BlogModel.objects.filter(slug=slug).first()
        
        if blog_obj:
            context['blog']=blog_obj
            context['profiles']=profile.objects.filter(user_name=request.user).first()
            return render(request,'blog_detail.html',context)
    except Exception as e:
        print("blog details    ",e)
        return HttpResponse("Erro 404 Not found")
    print(slug)
    return HttpResponse("Erro 404 Not found")

# def logout_user(request):
#     if request.method=='POST':
#         logout(request)
        
#         return redirect('homes')
def your_blogs(request):
    try:
        user_blogs_all=BlogModel.objects.filter(user=request.user)
        print("----------==============:  ",user_blogs_all,"   ",request.user)
        if user_blogs_all:
            context={}
            context['blogs']=user_blogs_all
            return render(request,'your_blogs.html',context)
        else:
            messages.error(request,"Plase add blog first")
            return redirect('add_blog')
    except Exception as e:
        print("yout blof   ",e)
    return render(request,'error.html')


def user_profile(request,token):
    return render(request,'error.html')

def account_verfication(request,token):
    print(token)
    verify_user=profile.objects.filter(token=token).first()
    if verify_user is not None:
        print("hello")
        verify_user.verify=True
        verify_user.save()
        messages.success(request,"All set now you can log in")
        return redirect('login')
    return render(request,'error.html')