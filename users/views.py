import json, jwt, requests

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