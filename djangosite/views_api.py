import email
from lib2to3.pgen2 import token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import profile
from .helpers import *
from django.contrib.auth import authenticate , login


class LoginView(APIView):     

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'somethig went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user is None:
                response['mesaage'] = 'invalid user name, user not found'
                raise Exception('invalid, user not found')

            user_obj = authenticate(username = data.get('username') , password = data.get('password'))

            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['mesaage'] = 'Welcome'
            else:
                response['mesaage'] = 'invalid password'
                raise Exception('invalid password')

        except Exception as e:
            print(e)

        return Response(response)    

LoginView = LoginView.as_view()

class SignupView(APIView):
    
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user:
                response['mesaage'] = 'username already taken'
                raise Exception('username already taken')

            if not profile.objects.filter(user = check_user).first().is_varified:
                response['message'] = 'your profile is not varified'
                raise Exception('profile not variefied')
                

            user_obj = User.objects.create(email = data.get('username') , username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            token = generate_random_string(20)
            profile.objects.create(user = user_obj , token = token)
            #send_mail_to_user(token , data.get('username'))
            response['message'] = 'User created'
            response['status'] = 200

        except Exception as e:
            print(e)

        return Response(response)    

SignupView =   SignupView.as_view()
