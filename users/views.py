import json, jwt, requests, bcrypt, re

from django.views import View
from django.http  import JsonResponse

from .models     import User
from my_settings import SECRET_KEY, ALGORITHM

class KakaoSigninView(View):
    def get(self,request):
        try:
            access_token = request.headers.get('Authorization')
            if not access_token:
                return JsonResponse({'message':'TOKEN_DOES_NOT_EXIST'},status=401)

            url     = "https://kapi.kakao.com/v2/user/me"
            headers = {'Authorization':f'Bearer {access_token}'}
            if not requests.get(url, headers=headers):
                return JsonResponse({'message':'INVALID_TOKEN'},status=401)

            response = requests.get(url, headers=headers).json()

            user, is_created = User.objects.get_or_create(
                    email       = response['kakao_account']['email'],
                    name        = response['kakao_account']['profile']['nickname'],
                    social_id   = response.get('id'),
                    signup_type = 'kakao'
                    )
            token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm=ALGORITHM)
            return JsonResponse({'token': token}, status = 200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class EmailSignupView(View):
    def post(self, request):
        try:
            email_regex     = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            password_regex  = re.compile('^(?=.*[A-Za-z!@#$%^&+=])(?=.*[!@#$%^&+=0-9])(?=.*[A-Za-z0-9]).{6,15}$')
            data            = json.loads(request.body)
            bcrypt_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if not email_regex.match(data['email']):
                return JsonResponse({'message':'INVALID_EMAIL'}, status=400)

            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'message': 'EMAIL_EXIST'}, status=400)

            if not password_regex.match(data['password']):
                return JsonResponse({'message':'INVALID_PASSWORD'},status=400)

            User.objects.create(
                    name        = data['name'],
                    email       = data['email'],
                    password    = bcrypt_password,
                    signup_type = "nomal"
                    )
            return JsonResponse({'message':'SUCCESS'},status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)

class EmailSigninView(View):
    def post(self,request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if not User.objects.filter(email=email).exists():
                return JsonResponse({'message':'INVALID_USER'},status=401)

            user = User.objects.get(email=email)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_PASSWORD'},status=401)

            access_token = jwt.encode({'id':user.id}, SECRET_KEY,ALGORITHM)

            return JsonResponse({'token': access_token, 'message': 'SUCCESS'}, status=200)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)



