import jwt

from django.http import JsonResponse

from .models             import User
from mywishtrip.settings import SECRET_KEY, ALGORITHM

def user_decorator(func):
	def wrapper(self, request, *args, **kwargs):
		try:
			access_token = request.headers.get('Authorization')
			data         = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
			user         = User.objects.get(id = data['id'])
			request.user = user

		except jwt.DecodeError:
				return JsonResponse({'message':'INVALID_TOKEN'}, status=401)

		except User.DoesNotExist:
			return JsonResponse({'message':'INVALID_USER'}, status=401)

		return func(self, request, *args, **kwargs)

	return wrapper
