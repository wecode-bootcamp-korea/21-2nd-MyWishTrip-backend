import json
import bcrypt

from django.test import TestCase, Client

from products.models import MainCategory, SubCategory, Region, Product, Option, Date
from users.models    import User
from unittest.mock   import MagicMock

from decimal  import Decimal
from datetime import datetime

class ReservationTastCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        MainCategory.objects.create(id=1,name='test')
        SubCategory.objects.create(id=1,name='test', maincategory_id=1)
        Region.objects.create(id=1,name='test')
        User.objects.create(
            id=1,email='test@test.com',
            name='test',
            password=bcrypt.hashpw('test123456789'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            )
        Product.objects.create(
            id=1,
            name='test',
            price=Decimal(123.00),
            discount=0.1,
            main_image='test',
            detail_image='test',
            subcategory_id=1,
            region_id=1
        )
        Option.objects.bulk_create(
            [
                Option(id=1, name='test', price=Decimal(1), product_id=1),
                Option(id=2, name='test2', price=Decimal(1), product_id=1)
            ]
        )
        Date.objects.bulk_create(
            [
                Date(id=1, date=datetime.strptime('2021-06-26', '%Y-%m-%d'), count=5, option_id=1),
                Date(id=2, date=datetime.strptime('2021-06-27', '%Y-%m-%d'), count=5, option_id=1)
            ]
        )

    def tearDown(self):
        User.objects.all().delete()
        MainCategory.objects.all().delete()
        SubCategory.objects.all().delete()
        Region.objects.all().delete()
        Product.objects.all().delete()
        Date.objects.all().delete()
        Option.objects.all().delete()
    
    def test_reservation_post(self):
        client = Client()

        body_data = {'reservations' : [{
            'option_id' : 1,
            'date_id'   : 1,
            'count'     : 1
        },
        {
            'option_id' : 1,
            'date_id'   : 2,
            'count'     : 1
        }
        ]}

        login_data = {
            'email' : 'test@test.com',
            'password' : 'test123456789'
        }
        
        login_response = client.post('/users/signin', json.dumps(login_data), content_type='application/json')
    
        headers = {
            'HTTP_Authorization' : login_response.json()['token'],
            'content_type' : 'application/json'
        }

        response = client.post('/reservations', json.dumps(body_data), **headers)
        
        self.assertEqual(response.json(), {'reservation':'SUCCESS'})
        self.assertEqual(response.status_code, 201)
