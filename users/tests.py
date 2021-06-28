import jwt, json ,bcrypt

from django.test         import TestCase, Client
from unittest.mock       import patch, MagicMock
from .models             import User
from mywishtrip.settings import SECRET_KEY, ALGORITHM

class KakaoTestCase(TestCase):
    @patch('users.views.requests')
    def test_kakao_signin(self, mock_requests):
	    client=Client()	
	    class MockedResponse:
	    	def json(self):
	    		return{
                    'id'            : 123333,
                    'kakao_account' : {
                    'profile'       : {
                    'nickname'      : '오옹'},
                    'email'         : 'king2@nate.com'}}

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
                'id'            : 123333,
                'kakao_account' : {
                'profile'       : {
                'nickname'      : '오옹'},
                'email'         : 'king2@nate.com'}}

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
                'id'            : 123333,
                'kakao_account' : {
                'profile'       : {
                'nickname'      : '오옹'}}}
    	mock_requests.get = MagicMock(return_value=MockedResponse())
    	headers           = {"HTTP_Authorization": "joke_token"}
    	response          = client.get("/users/social-login",**headers)

    	self.assertEqual(response.json(), {'message':'KEY_ERROR'})
    	self.assertEqual(response.status_code, 400)

    @patch('users.views.requests')
    def test_kakao_invalid_token(self,mock_requests):
    	client=Client()	
    	class MockedResponse:
    		def json(self):
    			return{
            'code':-401
				}
    	mock_requests.get = MagicMock(return_value=MockedResponse())
    	headers           = {"HTTP_Authorization": "joke_token"}
    	response          = client.get("/users/social-login",**headers)

    	self.assertEqual(response.json(), {'message':'INVALID_TOKEN'})
    	self.assertEqual(response.status_code, 401)

class EmailSignupCase(TestCase):
    def setUp(self):
        User.objects.create(
            name        = 'a',
            email       = 'aa@naver.com',
            password    = 'aa11!!',
            signup_type = 'nomal'
            )

    def tearDown(self):
        User.objects.all().delete()

    def test_signup_success(self):
        client = Client()
        user = {
            'name'        : 'b',
            'email'       : 'bb@naver.com',
            'password'    : 'aa11!!',
            'signup_type' : 'nomal'
        }
        response = client.post('/users/signup', json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{'message':'SUCCESS'})

    def test_invalid_email(self):
        client = Client()
        user = {
            'name'        : 'a',
            'email'       : 'aanaver.com',
            'password'    : 'aa11!!',
            'signup_type' : 'nomal'
        }
        response = client.post('/users/signup',json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json(), {'message':'INVALID_EMAIL'})
    
    def test_email_exist(self):
        client = Client()
        user = {
            'name'        : 'a',
            'email'       : 'aa@naver.com',
            'password'    : 'aa11!!',
            'signup_type' : 'nomal'
        }
        response = client.post('/users/signup',json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json(), {'message':'EMAIL_EXIST'})

    def test_invalid_password(self):
        client = Client()
        user = {
            'name'        : 'a',
            'email'       : 'bb@naver.com',
            'password'    : '11!!',
            'signup_type' : 'nomal'
        }
        response = client.post('/users/signup',json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json(), {'message':'INVALID_PASSWORD'})

    def test_key_error(self):
        client = Client()
        user = {
            '이름'         : 'a',
            'email'       : 'bb@naver.com',
            'password'    : 'aa11!!',
            'signup_type' : 'nomal'
        }
        response = client.post('/users/signup',json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json(), {'message':'KEY_ERROR'})

class EmailSigninCase(TestCase):
    def setUp(self):
        User.objects.create(
            name        = 'a',
            email       = 'aa@naver.com',
            password    = bcrypt.hashpw('aa11!!'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            signup_type = 'nomal'
            )

    def tearDown(self):
        User.objects.all().delete()

    def test_signin_success(self):
        client = Client()
        user   = {
            'email'    : 'aa@naver.com',
            'password' : 'aa11!!'
        }

        test_user    = User.objects.get(email='aa@naver.com')
        access_token = jwt.encode({'id':test_user.id},SECRET_KEY,ALGORITHM)
        response     = client.post('/users/signin',json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{'message':'SUCCESS','token':access_token})

    def test_invalid_user(self):
        client = Client()
        user = {
            'email'    : 'bb@naver.com',
            'password' : 'aa11!!'
        }
        response = client.post('/users/signin',json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),{'message':'INVALID_USER'})

    def test_invalid_password(self):
        client = Client()
        user = {
            'email'    : 'aa@naver.com',
            'password' : '1'
        }
        response = client.post('/users/signin',json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),{'message':'INVALID_PASSWORD'})

    def test_key_error(self):
        client = Client()
        user = {
            'name'     : 'a',
            'password' : 'aa11!!'
        }
        response = client.post('/users/signin',json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{'message':'KEY_ERROR'})