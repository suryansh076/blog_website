from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *


class loginview(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']="something went wrong"
        try:
            data=request.data
            if data.get('username') is None:
                response['message']='username is empty'
                raise Exception('Key is not found')
            if data.get('password') is None:
                response['message']='password is empty'
                raise Exception('password is not found')

            check_user=User.objects.filter(username=data.get('username')).first()
            if check_user is None:
                response['message']='Invalid user'
                raise Exception('No user is present')
            user_obj=authenticate(username=data.get('username'),password=data.get('password'))
            acc_verify=profile.objects.filter(user_name=check_user).first()
            if acc_verify.verify==False:
                response['message']='Verify your account !!'
                raise Exception('Account not verified')

            if user_obj:
                login(request,user_obj)
                response['status']=200
                response['message']='Welcome'
                login(request,user_obj)
                return JsonResponse("Login Successful")
            else:
                response['message']='Invalid password'
                raise Exception('Password is not valid ')
        except Exception as e:
            print(e)
        return Response(response)


class Registerview(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']="something went wrong"
        try:
            data=request.data
            if data.get('username') is None:
                response['message']='username is empty'
                raise Exception('user is not found')
            if data.get('password') is None:
                response['message']='password is empty'
                raise Exception('password is not found')

            check_user=User.objects.filter(username=data.get('username')).first()
            if check_user:
                response['message']='user already exist'
                raise Exception('user already exist')
            user_obj=User.objects.create_user(username=data.get('username'),password=data.get('password'),email="")
            user_obj.save()
            response['status']=200
            response['message']='UserCreated'
            return JsonResponse("You are successfully registred.")
         
        except Exception as e:
            print(e)
        return Response(response)

class logout_user(APIView):
    def post(self,request):
        response={}
        logout(request)
        response['status']=200
        response['message']='loggedout'
        return Response(response)