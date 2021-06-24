from django.http import response
import jwt, json 

from django.test   import TestCase, Client
from unittest.mock import patch, MagicMock
from .models       import User
from mywishtrip.settings import SECRET_KEY, ALGORITHM

class KakaoTestCase(TestCase):
	@patch('users.views.requests')
	def test_kakao_signin(self, mock_requests):
		client=Client()	
		class MockedResponse:
			def json(self):
				return{
					'id':123333,
					'kakao_account':{
						'profile':{
							'nickname' : '오옹'},
							'email'    : 'king2@nate.com'}}
		mock_requests.get = MagicMock(return_value=MockedResponse())
		headers           = {"HTTP_Authorization": "joke_token"}
		response          = client.get("/users/social-login", **headers)
		user              = User.objects.get(email='king2@nate.com')
		token             = jwt.encode({'id':user.id}, SECRET_KEY, ALGORITHM)

		self.assertEqual(response.json(), {'token' : token})
		self.assertEqual(response.status_code, 200)

	@patch('users.views.requests')
	def test_kakao_none_token(self, mock_requests):
		client=Client()
		class MockedResponse:
			def json(self):
				return{
					'id':123333,
					'kakao_account':{
						'profile':{
							'nickname' : '오옹'},
							'email'    : 'king2@nate.com'}}
		mock_requests.get = MagicMock(return_value=MockedResponse())
		response          = client.get("/users/social-login")

		self.assertEqual(response.json(), {'message':'TOKEN_DOES_NOT_EXIST'})
		self.assertEqual(response.status_code, 401)

	@patch('users.views.requests')
	def test_kakao_key_error(self,mock_requests):
		client=Client()	
		class MockedResponse:
			def json(self):
				return{
					'id':123333,
					'kakao_account':{
						'profile':{
							'nickname' : '오옹'},
							}}
		mock_requests.get = MagicMock(return_value=MockedResponse())
		headers           = {"HTTP_Authorization": "joke_token"}
		response          = client.get("/users/social-login",**headers)

		self.assertEqual(response.json(), {'message':'KEY_ERROR'})
		self.assertEqual(response.status_code, 400)
